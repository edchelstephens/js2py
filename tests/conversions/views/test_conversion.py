import json
import pprint

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from conversions.views.conversion import ConversionAPIView


class ConversionAPIViewTestCase(APITestCase):
    """ConversionAPIView test case."""

    maxDiff = None

    def setUp(self) -> None:
        self.request_factory = APIRequestFactory()
        self.view = ConversionAPIView.as_view()
        self.url = "conversions/js-to-python/"

    def test_post_successfully_converts_js_object_to_python(self) -> None:
        """Post successfully converts js object to python."""

        input_object = '{"id": 281,"code": null}'
        data = {"data": input_object}
        request = self.request_factory.post(self.url, data=data)
        response = self.view(request)

        raw_conversion = json.loads(input_object)
        expected_response_data = {
            "input_data": data.get("data"),
            "raw_conversion": raw_conversion,
            "prettified_conversion": pprint.pformat(raw_conversion),
        }

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data, expected_response_data)
