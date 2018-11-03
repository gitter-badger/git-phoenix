import json
from .parser import Parser


class JsonParser(Parser):

    def parse(self, file_path):
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
