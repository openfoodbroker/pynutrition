import json
import pprint
from ofb.math import deviation_ok
from ofb.nutrition import Nutrition

def recipe_has_valid_nutrition_data(recipe):
    keys = recipe.keys()
    mandatory_keys = ["fat", "protein", "calories", "sodium"]
    for mk in mandatory_keys:
        if mk not in keys:
            return False
        if recipe[mk] is None:
            return False


    return True


def recipe_passes_blacklist(recipe, blacklist):
    for declined_item in blacklist:
        if declined_item.lower() in json.dumps(recipe).lower():
            return False

    return True



def recipes_set_passes_nutrition_requirements_halved(energy_requirement, recipes, epsilon):

    assert len(recipes)==3, len(recipes)

    total_energy = 0
    total_fat = 0
    total_carbs = 0
    total_proteins = 0


    for r in recipes:

        total_energy = total_energy + r["calories"]
        total_proteins = total_proteins + r["protein"]
        #total_carbs = total_carbs + r["carbohydrates"]
        total_fat = total_fat + r["fat"]


    total_energy = total_energy/2
    total_proteins = total_proteins/2
    total_fat = total_fat/2

    energy_deviation_ok = deviation_ok(energy_requirement, total_energy, epsilon)

    if energy_deviation_ok:

        N = Nutrition()

        proportions = N.energy_split(total_energy)
        if deviation_ok(proportions["fat"], total_fat, epsilon) and deviation_ok(proportions["protein"], total_proteins, epsilon):
            # print("detected acceptable amounts of proteins and fat.")
            return True
        else:
            # print("mismatch on nutriment proportions")
            return False

    else:
        # print("mismatch on energy: computed day plan %s vs. requirement %s" % (total_energy, energy_requirement))
        return False


def recipes_set_passes_nutrition_requirements(energy_requirement, recipes, epsilon):

    assert len(recipes)==3 or len(recipes)==6 , len(recipes)

    total_energy = 0
    total_fat = 0
    total_carbs = 0
    total_proteins = 0


    for r in recipes:

        total_energy = total_energy + r["calories"]
        total_proteins = total_proteins + r["protein"]
        #total_carbs = total_carbs + r["carbohydrates"]
        total_fat = total_fat + r["fat"]

    energy_deviation_ok = deviation_ok(energy_requirement, total_energy, epsilon)

    if energy_deviation_ok:

        N = Nutrition()

        proportions = N.energy_split(total_energy)
        if deviation_ok(proportions["fat"], total_fat, epsilon) and deviation_ok(proportions["protein"], total_proteins, epsilon):
            # print("detected acceptable amounts of proteins and fat.")
            return True
        else:
            # print("mismatch on nutriment proportions")
            return False

    else:
        # print("mismatch on energy: computed day plan %s vs. requirement %s" % (total_energy, energy_requirement))
        return False
