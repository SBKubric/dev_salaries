import argparse
from constants import LanguagesSet
import json
import seaborn as sns
import pandas
import re


def parse_args():
    parser = argparse.ArgumentParser(description='The script prunes all info from loaded json object except title, salary and'
                                                 'requirements for a dev.')
    parser.add_argument('input', help='The name of the input file.')
    parser.add_argument('-o', '--output', default=None, help='The name of the output picture.')
    return parser.parse_args()


def load_json(filename: str) -> dict:
    with open(filename) as file_handler:
        return json.load(file_handler)


def is_language_required(language_pattern: str, vacancy: dict) -> bool:
    space_pattern = r"\b"
    language_pattern = '{}{}{}'.format(space_pattern, re.escape(language_pattern), space_pattern)
    has_in_title = not re.search(language_pattern, vacancy['title'], re.IGNORECASE) is None
    has_in_requirements = (vacancy['requirements'] and not re.search(language_pattern, vacancy['requirements'], re.IGNORECASE) is None)
    return has_in_title or has_in_requirements


def get_dataframe_for_plotting_average_salaries_bar_chart(json_vacancies: dict) -> pandas.DataFrame:
    languages_patterns = LanguagesSet.get_languages_patterns()
    statistics = LanguagesSet.get_languages_statistics_container()
    for vacancy in json_vacancies['objects']:
        for index, language_patterns in enumerate(languages_patterns):
            for language_pattern in language_patterns:
                if is_language_required(language_pattern, vacancy):
                    statistics[index]['count'] += 1
                    statistics[index]['salary'] += vacancy['salary']
                    break
    for language in statistics:
        if language['count']:
            language['salary'] = language['salary'] / language['count']  # mean value
    res_statistics = [
        {
            'Language': lang['lang'],
            'Avg. Salary (Roubles)': lang['salary'],
            'Vacancies Total': lang['count']
        } for lang in statistics
    ]

    df = pandas.DataFrame(res_statistics)
    df = df[df > 0]
    df = df.dropna(subset=['Vacancies Total'])
    return df


def plot_histogramm(data_frame: pandas.DataFrame, output: str):
    sns.set(style='white')
    sns.set_context('paper',
                    rc={"font.size": 8, "axes.titlesize": 8, "axes.labelsize": 12})
    g = sns.factorplot(x="Language", y="Avg. Salary (Roubles)", data=data_frame, kind="bar",
                       palette="deep", size=6, aspect=2)
    ax = g.ax

    def annotate_bars(row, ax=ax):
        for p in ax.patches:
            ax.annotate('{:.0f}'.format(p.get_height()),
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', fontsize=8, color='grey',
                        xytext=(0, 10),
                        textcoords='offset points')
    data_frame.apply(annotate_bars, ax=ax, axis=1)
    sns.plt.title("Data source: api.superjob.ru | "
                       "Author: Stanislav Bogatskiy (github.com/SBKubric)", fontsize=8)
    if output:
        g.savefig("output.png", bbox_inches="tight")


def analyze_salaries(json_vacancies: dict, output_filename=None):
    prepared_data = get_dataframe_for_plotting_average_salaries_bar_chart(json_vacancies)
    plot_histogramm(prepared_data, output_filename)


if __name__ == '__main__':
    args = parse_args()
    json_vacancies = load_json(args.input)
    analyze_salaries(json_vacancies, args.output)
