# Menu matcher

Menu matcher is a smart generator for personalized nutrition plans.

# How to use

This first implementation requires the following steps.

* Download example recipe [database](https://www.kaggle.com/hugodarwood/epirecipes).
* Save it under ```data/recipes-20000.json```.
* Edit your diet preferences in the ```config.yml```.
* Run ```python3 -m pytest -s tests/week_generator.py```


# Program configuration explained

Please consider the following three sections in ```config.yml```.

* Person
* Nutrition
* System

## Person

While most personal data is self-explaining, let's talk about the ```diet```
value. If set to ```1.0```, that means the program will compute 100% of
recommended nutrition.

```

person:
  age: 30
  sex: female
  height: 170
  weight: 75
  diet: 0.8

```

## Menu

Nutrition: in the no-go list, define things generally inacceptable.

The menu block is self-explaining; "style" can be of the following values:

* random - no limitations
* vegetarian - pick only recipes marked as vegetarian
* vegan - pick only recipes marked as vegan

```
monday:
  style: random
  like: ["lentils", "chicken", "salad"]
  dislike: ["garlic"]
```

## System

* Matching tolerance: set maximum acceptable deviation from target nutrition.
* Maximum iterations: how many attempts to match a menu should system take
* Data file: local recipes database
* Use recipe scale trick: for faster matching, a recipe can be halved
or doubled.

```
system:
  matching_tolerance: 0.07
  max_iterations: 150000
  data_file: "data/recipes-20000.json"
  use_recipe_scale_trick: true
```
