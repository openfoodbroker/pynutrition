import unittest
import yaml
from ofb.person import Person
from ofb.constants import SEX
from ofb.defaults import CONFIG_FILE
from ofb.nutrition import Nutrition
from ofb.helpers import load_json
import pprint


class TestPerson(unittest.TestCase):


    def setUp(self):

        self.persons = []

        data = {"sex":SEX.FEMALE, "age":41, "height":161, "weight": 89, "PAL": 1.5}
        data["diet"] = 0.8
        self.persons.append(Person(data))

        with open(CONFIG_FILE) as file:
            config = yaml.load(file, Loader=yaml.FullLoader)

        data = config["person"]
        pprint.pprint(data)
        self.persons.append(Person(data))


    def test_person(self):

        for p in self.persons:

            p.compute()
            p.validate()

            bmi = p.bmi
            energy = p.energy_requirement
            print("BMI: %s; energy requirement: %s" % (bmi, energy))

            pprint.pprint(p.nutrition)
            pprint.pprint(p.nutrition_diet)
            print("---------------")


if __name__ == '__main__':
    unittest.main()
