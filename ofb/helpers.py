""" Helper methods """

import pprint
import json
from itertools import repeat
from random import randint


def load_json(path):
    """Load json from file"""
    json_object = json.load(open(path))
    return json_object


def json_matches_list(json_object, mylist):
    """Check if json matches a keyword from a list"""
    for item in mylist:
        if item.lower() in json.dumps(json_object).lower():
            return True

    return False


def load_recipe_n(index, recipe_array):
    """Return N-th recipe in the database"""
    return (recipe_array[index])

def print_recipe_n(index, recipe_array):
    """Print N-th recipe in the database"""
    pprint.pprint(recipe_array[index])


def pick_random(target, data):
    """ pick target numnber of recipes randomly"""

    randoms = []
    recipes = []
    for _ in repeat(None, target):
        randoms.append(randint(0, len(data)-1))

    for recipe in randoms:
        recipes.append(data[recipe])

    return recipes
