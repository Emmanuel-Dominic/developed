from signal import raise_signal
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_zipcode(value):
    if len(value) != 4:
        raise ValidationError(_("Field needs to be of length 4: %{value}s"), code='invalid_length', params={'value': value})
