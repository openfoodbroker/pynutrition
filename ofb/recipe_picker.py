from ofb.helpers import json_matches_list
from random import randint
import pprint


class RecipePicker:

    def __init__(self, config):
        self.config = config

    def eval_recipe_blacklisted(self, recipe, day_config):
        if "dislike" not in day_config.keys():
            return False
        return json_matches_list(recipe, day_config["dislike"])

    def eval_recipe_whitelisted(self, recipe, day_config):
        if "like" not in day_config.keys():
            return True
        return json_matches_list(recipe, day_config["like"])

    def eval_recipe_matches_meta_category(self, recipe, day_config):
        pass

    def eval_recipe_matches_categories(self, recipe, day_config):
        if "categories" not in day_config.keys():
            return True
        # step 1 match recipe data categories
        categories = recipe["categories"]
        categories = [x.lower() for x in categories]
        for c_user in self.config["nutrition"]["categories"]:
            if c_user not in categories:
                return False

    def eval_recipe_matches_style(self, recipe, day_config):
        if "style" not in day_config.keys():
            return True

        if  day_config["style"] in ["random", "any", "all", "everything"]:
            return True

        # print("match style: %s" % day_config["style"])
        # step 1 match recipe data categories
        categories = recipe["categories"]
        categories = [x.lower() for x in categories]
        for c in categories:
            if day_config["style"] == c:
                return True
        return False


    def pick(self, day_config, data):

        for attempts in range(5*len(data)):
            pick_index = randint(0, len(data)-1)

            recipe = data[pick_index]

            # print("RECIPE EVAL:")
            # print("%s %s %s" % (self.eval_recipe_matches_style(recipe, day_config), self.eval_recipe_blacklisted(recipe, day_config) , self.eval_recipe_whitelisted(recipe, day_config)))

            if self.eval_recipe_matches_style(recipe, day_config) and self.eval_recipe_blacklisted(recipe, day_config) is False and self.eval_recipe_whitelisted(recipe, day_config):

                return recipe

        raise Exception("Try to rerun the program or make your search criteria broader. Or did you mistype anything?")


    def reduce_data(self, data, blacklist):
        new_dataset = []

        for recipe in data:
            if json_matches_list(recipe, blacklist):
                new_dataset.append(recipe)

        return new_dataset
