import argparse
import json
import os
import requests
from urlencoder import urlencode


def parse_args():
    parser = argparse.ArgumentParser(description='The script fetches vacancies list from api.superjob.ru and dumps it to'
                                                 'json file.\nYou need to provide an API key for this script by exporting'
                                                 'an environment variable <SJ_API_KEY>\n')
    parser.add_argument('filename', help='The name of output file.')
    return parser.parse_args()


def fetch_vacancies_json() -> dict:
    api_key = os.getenv('SJ_API_KEY', 'NOT FOUND')
    if api_key == 'NOT FOUND':
        raise EnvironmentError('The environment variable SJ_API_KEY is not set!')
    headers = {'X-Api-App-Id': api_key}
    vacancies_url = 'https://api.superjob.ru/2.0/vacancies/'
    params = {
        'town': 4,
        'catalogues': 48,
        'count': 100,
        'no_agreement': 1,
        'keywords': [
            [10, 'or', 'Программист'],
            [10, 'or', 'Разработчик'],
            [10, 'or', 'Developer'],
            [10, 'or', 'Software Engineer'],
            [10, 'or', 'Инженер'],
            [10, 'nein', 'Аналитик'],
            [10, 'nein', 'Директор'],
            [10, 'nein', 'Менеджер'],
            [10, 'nein', 'Консультант'],
        ]
    }
    params = urlencode(params)
    return json.loads(
        requests.get('{}?{}'.format(vacancies_url, params), headers=headers).text)


def dump_json_to_file(filename: str, json_object: dict):
    with open(filename, mode='w') as file_handler:
        return json.dump(json_object, file_handler)


if __name__ == '__main__':
    args = parse_args()
    json_vacancies = fetch_vacancies_json()
    dump_json_to_file(args.filename, json_vacancies)
