import pytest
import pprint
import json
import yaml


from ofb.helpers import load_json
from ofb.helpers import print_recipe_n
from ofb.helpers import load_recipe_n

DATAFILE="data/recipes-20000.json"

def test_print_recipe_n():
    json_object = load_json(DATAFILE)
    print_recipe_n(33, json_object)

def test_load_recipe_n():
    json_object = load_json(DATAFILE)
    recipe = load_recipe_n(33, json_object)
    pprint.pprint(recipe)


def test_config_reader():
    with open(r'config/config.yml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    pprint.pprint(config)
    pprint.pprint(config["nutrition"]["menu"]["friday"])
