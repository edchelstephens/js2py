from django.forms import ModelForm

from conversions.models.conversion import Js2PyConversion

class Js2PyConversionForm(ModelForm):
    """Js2PyConversion Model form."""

    class Meta:
        model = Js2PyConversion
        fields = ["data"]