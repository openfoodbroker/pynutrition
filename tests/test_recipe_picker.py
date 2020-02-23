import pprint
import unittest
import yaml
from ofb.nutrition import Nutrition
from ofb.helpers import load_json
from ofb.recipe_picker import RecipePicker

DATAFILE="data/recipes-20000.json"

class RecipePickerTestCase(unittest.TestCase):

    def setUp(self):
        json_object = load_json(DATAFILE)

        with open(r'config/config.yml') as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader)

        N = Nutrition()

        self.data = N.enhance_data(json_object, self.config)
        self.rp = RecipePicker(self.config)

    def test_pick(self):

        energy_requirement = 1500
        day = self.config["nutrition"]["menu"]["monday"]
        recipe = self.rp.pick(day, self.data)

        pprint.pprint(recipe)
        print(recipe["title"])
