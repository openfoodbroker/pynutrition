""" Person class """

from ofb.constants import SEX
import pprint

class Person:
    """Class definition"""

    def __init__(self, data):
        assert data["sex"] is "male" or "female", "sex has value %s" % data["sex"]
        self.sex = data["sex"]
        self.age = data["age"]
        self.height = data["height"]
        self.weight = data["weight"]
        self.pal = data["PAL"]
        self.diet = data["diet"]

        self.nutrition = {}
        self.nutrition_diet = {}
        self.bmi = None


    def compute(self):
        self.bmi = self.calc_BMI()
        self.energy_requirement = self.calc_energy_requirement()
        nutrition = self.calc_nutrition(self.energy_requirement)
        self.nutrition = nutrition
        self.energy_requirement_diet = self.energy_requirement * self.diet
        self.nutrition_diet = self.calc_nutrition(self.energy_requirement_diet)



    def validate(self):
        # validate WHO recommended protein RDA:
        # https://www.healthline.com/nutrition/how-much-protein-per-day
        # https://www.gofeminin.de/abnehmen/wieviel-eiweiss-pro-tag-s1369767.html
        # => 0.8 to 2 g / kg both sexes
        who_protein_minumum = 0.8 * self.weight
        who_protein_maximum = 2 * self.weight

        print("Protein check: WHO [%s-%s]g vs. target diet %s vs. this algo's RDA %s" %
             (who_protein_minumum, who_protein_maximum,
             self.nutrition_diet["protein"],
             self.nutrition["protein"] ))

        assert who_protein_minumum <= self.nutrition["protein"]  <= who_protein_maximum, "possibly some core logic error"

        if who_protein_minumum >= self.nutrition_diet["protein"]:
            print("WARNING: your current diet setting introduces a protein deficit of %s g" % (who_protein_minumum-self.nutrition_diet["protein"]))

        if self.nutrition_diet["protein"] >= who_protein_maximum:
            print("WARNING: your current diet setting introduces a protein excess of %s" % (self.nutrition_diet["protein"]-who_protein_maximum))



    def calc_BMI(self):
        """ BMI = Body Mass Index """
        assert 100 <= self.height <= 230, "check height value/units %s cm?" % self.height
        assert 20 <= self.weight <= 150, "check weight value/units %s kg?" % self.self.weight
        self.height = self.height /100
        self.bmi = self.weight/(self.height * self.height)
        return self.bmi

    def calc_BMR(self):
        """ WHO formula http://www.ernaehrung.de/tipps/allgemeine_infos/ernaehr10.php """
        megajoule = 0
        age = self.age
        weight = self.weight
        if self.sex == "SEX.MALE":
            if age <= 3:
                megajoule = 0.249 * weight - 0.127
            elif 3 < age <= 10:
                megajoule = 0.095 * weight + 2.110
            elif 11 <= age <= 18:
                megajoule = 0.074 * weight + 2.754
            elif 19 <= age <= 30:
                megajoule = 0.063 * weight +  2.896
            elif 31 <= 60:
                megajoule = 0.048 * weight + 3.653
            elif age > 60:
                megajoule = 0.049 * weight + 2.459

        else:
            if age <= 3:
                megajoule = 0.244 * weight - 0.130
            elif 3 < age <= 10:
                megajoule = 0.085 * weight + 2.033
            elif 11 <= age <= 18:
                megajoule = 0.056 * weight + 2.898
            elif 19 <= age <= 30:
                megajoule = 0.062 * weight +  2.036
            elif 31 <= 60:
                megajoule = 0.034 * weight + 3.538
            elif age > 60:
                megajoule = 0.038 * weight + 2.755

        assert megajoule * 239 > 0 and megajoule <= 1500

        return megajoule * 239


    def calc_WMR(self):
        """Total requirement depending on PAL = physical activity level"""
        return self.calc_BMR() * (self.pal - 1)

    def calc_energy_requirement(self):
        """ compute diet requirement"""
        BMR = self.calc_BMR()
        WMR = self.calc_WMR()
        return BMR + WMR

    def calc_nutrition(self, calories):
        return {"protein": calories*0.15/4, "fat": calories*0.3/9, "carbs": calories*0.55/4}


    def calc_energy_requirement_diet(self):
        return self.calc_energy_requirement() * self.diet
