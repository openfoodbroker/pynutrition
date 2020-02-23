"""Math helper functions"""

import operator as op
from functools import reduce
from ofb.constants import SEX


def nck(nval, kval):
    """from https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python"""
    # https://en.wikipedia.org/wiki/Binomial_coefficient"""
    # Computes the binomial coefficient n choose k"""
    kval = min(kval, nval-kval)
    numer = reduce(op.mul, range(nval, nval-kval, -1), 1)
    denom = reduce(op.mul, range(1, kval+1), 1)
    return numer / denom


def deviation_ok(norm, value, epsilon):
    """Check if a value's deviation from given norm stays under boundary"""
    deviation = abs(norm-value)/norm
    # print(abs(d-epsilon))
    return deviation <= epsilon


# Grundumsatz = BMR = Basic Metabolic Rate
# Leistungsumsatz Grundumsatz x (PAL-Faktor – 1) = WMR
def calc_energy_requirement(sex, age, weight, height, PAL):
    BMR = calc_bmr_who(sex, age, weight)
    WMR = calc_wmr(BMR, PAL)
    return BMR + WMR


def calc_wmr(BMR, PAL):
    """Total requirement depending on PAL = physical activity level"""
    return BMR * (PAL - 1)


# https://en.wikipedia.org/wiki/Basal_metabolic_rate
# https://bewusstgesund.at/kalorien-tagesumsatz-berechnen/
# https://en.wikipedia.org/wiki/Physical_activity_level


def physical_activity_level(sex, age, weight):
    if 3 <= age <= 16:
        return 0.025 * age + 1.40 # not clear: the actual activity impact on PAL
    raise Exception("for this input, PAL function is not implemented yet. Use fixed numbers.")
    # children 3-16  PAL: 0.025 x age+1.40.
    #https://www.researchgate.net/publication/10797427_Physical_activity_levels_in_children_and_adolescents
