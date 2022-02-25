from rest_framework.serializers import ModelSerializer

from conversions.models.conversion import Js2PyConversion

class Js2PyConversionSerializer(ModelSerializer):
    """Js2PyConversion model serializer."""

    class Meta:
        model = Js2PyConversion
        fields = ["data"]