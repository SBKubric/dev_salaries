import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser(description='The script prunes all info from loaded json object except title, salary and'
                                                 'requirements for a dev.')
    parser.add_argument('input', help='The name of the input file.')
    parser.add_argument('output', help='The name of the output file.')
    return parser.parse_args()


def load_json(filename: str) -> dict:
    with open(filename) as file_handler:
        return json.load(file_handler)


def prune_vacancies(json_vacancies: dict) -> dict:
    pruned_vacancies_list = []
    for json_object in json_vacancies['objects']:
        obj = {
            'title': json_object['profession'],
            'salary': max((json_object['payment_to'], json_object['payment'], json_object['payment_from'])),
            'requirements': json_object['candidat']
        }
        pruned_vacancies_list.append(obj)

    return {'objects': pruned_vacancies_list}


def dump_json_to_file(filename: str, json_object: dict):
    with open(filename, mode='w') as file_handler:
        return json.dump(json_object, file_handler)


if __name__=='__main__':
    args = parse_args()
    json_vacancies = load_json(args.input)
    pruned_vacancies = prune_vacancies(json_vacancies)
    dump_json_to_file(args.output, pruned_vacancies)
