from django.db import models
from pint import Unit
from . import ureg
from . import validators


class PintUnitField(models.CharField):

    def __init__(self, max_length=50, *args, **kwargs):
        super().__init__(max_length=max_length, *args, **kwargs)
        self.validators.append(validators.UnitValidator())

    def value_from_object(self, obj):
        """Return the value of this field in the given model instance."""
        val = getattr(obj, self.attname)
        return self.to_python(value=val)

    def get_prep_value(self, value):
        return value if value else str(ureg.count)

    def from_db_value(self, value, expression, connection):
        return getattr(ureg, value) if value else ureg.count

    def to_python(self, value):
        if isinstance(value, Unit) or value is None:
            return value
        return getattr(ureg, value)
