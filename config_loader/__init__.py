import io
import json


def get(variable):
    try:
        with io.open('config.json', "r", encoding='UTF-8') as file:
            keys = json.load(file)
            if variable in keys:
                return keys[variable]
            return None
    except FileNotFoundError:
        return None
