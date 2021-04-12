import json

class json_to_byte:

    def __init__(self):
        pass

    def convert(self, value):
        json = value.encode('utf-8').replace("'", '"')
        return json