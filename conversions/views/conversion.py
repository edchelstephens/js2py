from rest_framework.response import Response
from rest_framework.views import APIView

from conversions.models.conversion import Js2PyConversion


class ConversionAPIView(APIView):
    """Javascript to Python object conversion api view."""

    def post(self, request, *args, **kwargs):
        """Convert input javascript object string to python object api."""
        try:
            data = request.data
            input_data = data.get("data")

            conversion = Js2PyConversion(data=input_data)
            conversion.save()

            response = {
                "input_data": data.get("data"),
                "raw_conversion": conversion.get_python_conversion(),
                "prettified_conversion": conversion.get_prettified_python_conversion(),
            }
            return Response(response, status=200)

        except Exception as exc:
            error_response = {
                "title": "Error",
                "message": "Error on conversion",
                "error": str(exc),
            }
            return Response(error_response, status=400)
