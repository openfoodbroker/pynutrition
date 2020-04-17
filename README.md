# Menu matcher

Menu matcher is a smart generator for personalized nutrition plans.

# Note for non-programmer users

Please post an issue if any of the following steps is not clear enough.

You need the following prerequisites:

* If you are into trying out programming, to get the latest version, you'll need the tool *git* and run ```git clone https://github.com/openfoodbroker/pynutrition.git```. If not, just download a ZIP package from the [releases page](https://github.com/openfoodbroker/pynutrition/releases). 
* A PC (personal computer) with any popular operation system
* Install recent version of the [Python](https://www.python.org/downloads/) programming language.
* Install a code editor like Atom either Notepad++ or similar.
* If needed, take a couple of minutes to focus on running commands in the system console while having an eye on the execution path.
* To install program dependencies, run ```pip3 install - requirements.txt``` in the program folder.
* Now you are all set!

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
