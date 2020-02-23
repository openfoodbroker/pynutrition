"""Menu matcher: select a day menu plan with optimal nutrients"""
# from ofb.helpers import pick_random
from ofb.nutrition import Nutrition
from ofb.recipevalidators.validators import recipes_set_passes_nutrition_requirements
from ofb.recipevalidators.validators import recipes_set_passes_nutrition_requirements_halved
from ofb.recipe_picker import RecipePicker
# import pprint

class MenuMatcher:
    """Match day menu"""
    def __init__(self, data, energy_requirement, config):

        self.max_iterations = config["system"]["max_iterations"]
        self.data = data
        self.energy_requirement = energy_requirement
        self.config = config


    def get_day_menu(self, day_config):
        """create menu plan for a day"""
        # pprint.pprint(day_config)

        attempt_counter = 0
        total_energy = 0
        total_fat = 0
        # total_carbs = 0
        total_proteins = 0


        recipe_picker = RecipePicker(self.config)
        # seed_recipe = recipe_picker.pick(day_config, self.data)

        for _ in range(self.max_iterations):
            # print(t)
            attempt_counter = attempt_counter + 1
            if attempt_counter % 2500 == 0:
                print("Checked %s/%s menu plans for this day." % (attempt_counter, self.max_iterations))


            recipes = []
            for _ in range(3):
                recipes.append(recipe_picker.pick(day_config, self.data))


            scaling = 1
            epsilon = self.config["system"]["matching_tolerance"]
            if recipes_set_passes_nutrition_requirements(self.energy_requirement, recipes, epsilon):
                    nutrients = self.add_nutrients(recipes)
                    break
            else:
                # print("pick series %s -> mismatch" % t)
                if self.config["system"]["use_recipe_scale_trick"]:
                    if recipes_set_passes_nutrition_requirements(self.energy_requirement, recipes+recipes, epsilon):
                        # print("DOUBLE PLAN!")
                        scaling = 2
                        for recipe in recipes+recipes:
                            total_energy = total_energy + recipe["calories"]
                            total_proteins = total_proteins + recipe["protein"]
                            #total_carbs = total_carbs + r["carbohydrates"]
                            total_fat = total_fat + recipe["fat"]
                            # print("%s - %s kcal" % (r["title"], r["calories"]))


                        break


                    if recipes_set_passes_nutrition_requirements_halved(self.energy_requirement, recipes, epsilon):
                        # print("HALVE PLAN!")
                        scaling = 0.5
                        for recipe in recipes:
                            total_energy = total_energy + recipe["calories"]/2
                            total_proteins = total_proteins + recipe["protein"]/2
                            #total_carbs = total_carbs + r["carbohydrates"]
                            total_fat = total_fat + recipe["fat"]/2
                            # print("%s - %s kcal" % (r["title"], r["calories"]))


                        break

        plan_text = self.concat_menu_text(recipes, scaling)
        return {"menu":plan_text,
                "total_energy":total_energy,
                "total_fat":total_fat,
                "total_proteins": total_proteins,
                "attempt_counter": attempt_counter,
                "recipes": recipes,
                "scaling": scaling}

    @staticmethod
    def concat_menu_text(recipes, scaling):
        """create display tect for the menu printout"""
        menu = []
        for recipe in recipes:
            menu.append(recipe['title'])

        plan_text = " ;\n ".join(menu)
        scaling_info = ""
        if scaling == 2:
            scaling_info = "*x2!* "
        elif scaling == 0.5:
            scaling_info = "*½!* "
        return scaling_info + plan_text

    @staticmethod
    def add_nutrients(recipes, scale=1):
        """add nutrients using scale"""
        total_energy = 0
        total_fat = 0
        total_proteins = 0
        for recipe in recipes+recipes:
            total_energy = total_energy + recipe["calories"]*scale
            total_proteins = total_proteins + recipe["protein"]*scale
            #total_carbs = total_carbs + r["carbohydrates"]
            total_fat = total_fat + recipe["fat"]*scale

        return {"fat":total_fat,
                "proteins":total_proteins,
                "energy":total_energy}
