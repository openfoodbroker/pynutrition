"""Abstract datasource for recipes"""

from os import path
import json


class Datasource:
    """foo"""
    def __init__(self, data):

        self.name = data["name"]
        self.text = data["text"]
        self.url = data["url"]
        self.local = data["local"]

    def validate(self):
        """Prove that data source is valid"""
        if path.exists(self.local) is False:
            errmsg_part1 = "missing local data source file %s;"
            errmsg_part2 = "please download it from %s"
            err = errmsg_part1 + errmsg_part2
            raise Exception(err % (self.local, self.url))

        return True


    def load_local_json(self):
        """Load json structure from file"""
        json_object = json.load(open(self.local))
        return json_object
