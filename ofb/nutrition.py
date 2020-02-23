import json
class Nutrition:

    """Healthy nutrition model according to """
    """ http://www.ernaehrung.de/tipps/allgemeine_infos/ernaehr13.php """
    """ Takes energy target, splits it proportionally and then converts energy amounts to grams."""
    """ We assume here average values: 1g of carbs either proteins make 4 kcal, and 1g of fat makes 9 kcal"""
    """ As suggested at https://healthyeating.sfgate.com/gives-energy-per-gram-fat-protein-carbohydrates-8319.html"""
    def energy_split(self, calories):
        return {"protein": calories*0.15/4, "fat": calories*0.3/9, "carbs": calories*0.55/4}


    """Recommended intakes in milligrams"""
    """https://www.dge.de/presse/pm/dge-aktualisiert-die-referenzwerte-fuer-natrium-chlorid-und-kalium/"""
    def recommended_daily_nutrition(self):
        return {"sodium":1500}



    def eval_ingredients_overflow(self, recipe, config):
        if "max_ingredients" not in config["system"].keys():
            return False
        ingredients_count = len(recipe["ingredients"])
        allowed_max = config["system"]["max_ingredients"]
        if ingredients_count >= allowed_max:
            return True
        else:
            return False


    """ Reduce recipes data set by the NOGO-List and sparse nutrition data"""
    def enhance_data(self, data, config):

        nogolist = config["nutrition"]["nogolist"]
        new_dataset = []

        for recipe in data:
            if self.recipe_has_valid_nutrition_data(recipe) and self.recipe_passes_blacklist(recipe, nogolist):
                if self.eval_ingredients_overflow(recipe, config) is False:
                    new_dataset.append(recipe)


        return new_dataset


    def recipe_passes_blacklist(self, recipe, blacklist):
        for declined_item in blacklist:
            if declined_item.lower() in json.dumps(recipe).lower():
                return False

        return True

    def recipe_has_valid_nutrition_data(self, recipe):
        keys = recipe.keys()
        mandatory_keys = ["fat", "protein", "calories", "sodium"]
        for mk in mandatory_keys:
            if mk not in keys:
                return False
            if recipe[mk] is None:
                return False


        return True


    def recipe_matches_style(recipe, day_config):
        style = day_config["style"]
