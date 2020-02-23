from ofb.datasource import Datasource
from ofb.defaults import CONFIG_FILE, DATAFILE


def test_datasource():


    datasource = Datasource({"name":"Recipe database", "text":"Recipe database", "url":"https://www.kaggle.com/hugodarwood/epirecipes/download",
                             "local":DATAFILE})
    datasource.validate()
