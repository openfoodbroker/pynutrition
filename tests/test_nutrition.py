import pytest
import yaml
import pprint
from ofb.nutrition import Nutrition
from ofb.helpers import load_json
from ofb.defaults import DATAFILE, CONFIG_FILE



def test_energy_split():
    N =  Nutrition()
    spl = N.energy_split(1476)
    assert "fat" in spl.keys()
    pprint.pprint(spl)

def test_enhance_data():
    json_object = load_json(DATAFILE)
    len1 = len(json_object)

    with open(CONFIG_FILE) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    N = Nutrition()

    data = N.enhance_data(json_object, config)
    len2 = len(data)
    print("reduced data from %s to %s items." % (len1, len2))
