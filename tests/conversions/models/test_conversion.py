from django.test import TestCase

from conversions.models import Js2PyConversion


class Js2PyConversionModelTest(TestCase):
    """Js2PyConversion model test suite."""

    def setUp(self) -> None:
        """Run this setUp for each test."""
        self.input_data = "1"
        self.conversion = Js2PyConversion(data=self.input_data)

    def test_str(self) -> None:
        """Test str method."""

        expected = str(self.input_data)

        assert self.conversion.__str__() == expected
        assert str(self.conversion) == expected

    def test_repr(self) -> None:
        """Test repr method."""

        expected = "Js2PyConversion(data={})".format(repr(self.input_data))

        assert self.conversion.__repr__() == expected
        assert repr(self.conversion) == expected
