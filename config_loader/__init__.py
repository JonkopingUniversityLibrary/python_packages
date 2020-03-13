import io
import json


class ConfigLoaderException(Exception):
    """Custom docstring"""


class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.variables = self.load_variables()

    def load_variables(self):
        try:
            with io.open(self.config_file, "r", encoding='UTF-8') as file:
                keys = json.load(file)
                return keys
        except FileNotFoundError:
            raise ConfigLoaderException('No configuration file found.')

    def get(self, variable):
        if variable in self.variables:
            return self.variables[variable]
        else:
            return None
