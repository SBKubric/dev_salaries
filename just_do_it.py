from fetch_vacancies import fetch_vacancies_json
from prune_vacancies import prune_vacancies
from analyze_salaries import analyze_salaries
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='This script fetches data about software developers vacancies '
                                                 'from api.superjob.ru and builds a histogramm of average salary per'
                                                 'programming language.')
    parser.add_argument('-o', '--output', help='The name of output image.')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    vacancies_json = fetch_vacancies_json()
    vacancies_json = prune_vacancies(vacancies_json)
    analyze_salaries(vacancies_json, args.output)
