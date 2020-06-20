# django-pint-unit-field

This package provides a custom field to make use of the Unit class provided by
pint https://pypi.org/project/Pint/

Original idea is from https://github.com/bharling/django-pint but in this package
the amount is also stored.

** NOT SUITED FOR PRODUCTION ** This is a WIP, and it has not been tested properly.

###### Install this app
`git clone git@github.com:marcosalcazar/django-pint-unit-field.git`

###### Usage
Add the field to your models
```
from pintunitfield.fields import PintUnitField

class TheClass(models.Model): 
    attribute = PintUnitField() # max_length is optional, 50 is de default value
```

###### Test

** Inside virtualenv **
```
pip install -r test_requirements.txt
python runtests.py
```
