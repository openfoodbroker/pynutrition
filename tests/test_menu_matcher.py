import pytest
import yaml
import pprint
from ofb.defaults import CONFIG_FILE, DATAFILE
from ofb.helpers import load_json
from ofb.menu_matcher import MenuMatcher
from ofb.nutrition import Nutrition
from ofb.person import Person




def test_menu_matcher():

    data = load_json(DATAFILE)
    with open(CONFIG_FILE) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    N = Nutrition()

    data = N.enhance_data(data, config)

    person = Person(config["person"])
    person.compute()
    person.validate()

    energy_requirement = person.energy_requirement_diet

    day = config["nutrition"]["menu"]["monday"]

    mm = MenuMatcher(data, energy_requirement, config)
    pprint.pprint(mm.get_day_menu(day))
