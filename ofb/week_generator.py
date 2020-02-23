from beautifultable import BeautifulTable
from ofb.menu_matcher import MenuMatcher
from ofb.nutrition import Nutrition
from ofb.math import nck
import sys
import os.path
from os import path
import yaml
from ofb.helpers import load_json
from ofb.shoppinglist import ShoppingList
from ofb.person import Person


"""Week plan generator"""
class WeekGenerator:
    def __init__(self, datasource, config_file="config/config.yml"):

        # identify config file location
        config_file = "config/config.yml"
        if not path.exists(config_file):
            Exception("can't determine where config_file %s is." % config_file)

        with open(config_file) as file:
            config = yaml.load(file, Loader=yaml.FullLoader)

        self.person = Person(config["person"])

        # load data
        datasource.validate()
        data = load_json(datasource.local)

        N = Nutrition()
        data = N.enhance_data(data, config)

        self.x = BeautifulTable()
        self.x.column_headers = ["Position","Menu", "Energy", "Protein", "Fat", "Search attempts", ""]
        self.x.column_alignments['Menu'] = BeautifulTable.ALIGN_LEFT

        # combinations = nck(len(data), 3)
        print("By your no-go's list, the program will consider %s recipes." % (len(data)))
        print("For each day, we will try up to %s times per week day to find a plan matching your preferences." % config["system"]["max_iterations"])
        print("")
        self.config = config
        self.data = data

        self.shp = ShoppingList()


    def generate(self):


        N = Nutrition()
        normal_requirement = self.person.calc_energy_requirement()
        energy_requirement =  normal_requirement * self.config["person"]["diet"]
        print("normal diet %s, setting to %s" % (normal_requirement, energy_requirement))
        energy_splitted = N.energy_split(energy_requirement)

        self.x.append_row(["Required",
                      "ε ≤ %s"%self.config["system"]["matching_tolerance"],
                      energy_requirement,
                      energy_splitted["protein"],
                      energy_splitted["fat"], "",""])

        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print("")
        for day_of_week in week:
            print("%s.. " % day_of_week )


            day_configuration = self.config["nutrition"]["menu"][day_of_week.lower()]
            day_plan = self.get_day_menu(energy_requirement,  day_configuration, self.data)
            style = day_configuration["style"]
            if style == "vegan":
                style = "vv"
            if style == "vegetarian":
                style = "v"
            if style =="random":
                style =""
            self.x.append_row([day_of_week, day_plan["menu"], day_plan["total_energy"], day_plan["total_proteins"], day_plan["total_fat"], day_plan["attempt_counter"], style])
            #print("")

    def get_day_menu(self, energy_requirement, day_configuration, data):
        mm = MenuMatcher(self.data, energy_requirement, self.config)
        menu = mm.get_day_menu(day_configuration)
        recipes = menu["recipes"]

        for rcp in recipes:
            self.shp.add(rcp["ingredients"])

        return menu

    def render(self):
        self.shp.render()
        print(self.x)
