import pint
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

from . import ureg


@deconstructible
class UnitValidator:
    message = _('Enter a valid unit.')
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        """
        Validate that the input is a valid unit in the registry
        """
        if value:
            try:
                getattr(value, ureg)
            except pint.errors.UndefinedUnitError:
                raise ValidationError(self.message, code=self.code)
