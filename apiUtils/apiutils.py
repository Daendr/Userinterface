import json
import requests
from models.user import User
from typing import Type


class ApiUtils:

    @staticmethod
    def post(base_url, url_parts, data):
        response = requests.post(base_url+url_parts, data)

        return response

    @staticmethod
    def get(base_url, url_parts):
        response = requests.get(base_url+url_parts)
        return response

    @staticmethod
    def is_content_type_json(response):
            response.raise_for_status()
            content_type = response.headers.get('content-type')
            return 'application/json' in content_type

    @staticmethod
    def is_sort_by_value(response, value):
        posts = json.loads(response.text)
        posts_list = [post[value] for post in posts]
        return posts_list == sorted(posts_list)

    @staticmethod
    def get_expected_data(data_type: Type, data_source):
        if isinstance(data_source, str):
            with open(data_source, "r", encoding="utf-8") as file:
                data_dict = json.load(file)
        elif isinstance(data_source, dict):
            data_dict = data_source
        else:
            raise ValueError("Неподдерживаемый тип источника данных.")
        return data_type.from_dict(data_dict)

    @staticmethod
    def get_value(responce, value, content_type):
        _list = json.loads(responce.text)
        elem = next((elem for elem in _list if elem.get(content_type) == value), None)
        return User.from_dict(elem)
