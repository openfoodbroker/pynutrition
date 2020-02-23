import pytest
import yaml
import pprint
from ofb.helpers import load_json
from ofb.week_generator import WeekGenerator
from ofb.nutrition import Nutrition
from ofb.datasource import Datasource
from ofb.defaults import CONFIG_FILE, DATAFILE

def test_week_generator():

    datasource = Datasource({"name":"Recipe database", "text":"Recipe database", "url":"https://www.kaggle.com/hugodarwood/epirecipes",
                             "local":DATAFILE})


    wgr = WeekGenerator(datasource)
    wgr.generate()
    wgr.render()
