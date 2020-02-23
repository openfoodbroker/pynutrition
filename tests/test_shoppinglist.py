import pytest
from ofb.shoppinglist import ShoppingList
import json
from itertools import repeat
import pprint
from random import randint

from ofb.helpers import load_recipe_n
from ofb.helpers import load_json

from ofb.defaults import DATAFILE


def test_shoppinglist():
    shp = ShoppingList()

    json_object = load_json(DATAFILE)

    for _ in range(0, 3):
        pick_index = randint(0, len(json_object)-1)
        recipe = load_recipe_n(pick_index, json_object)
        if "ingredients" not in recipe.keys():
            continue
        shp.add(recipe["ingredients"])

    shp.render()
