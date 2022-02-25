import json
import pprint
from typing import Any

from django.db import models


class Js2PyConversion(models.Model):
    """Javascript object to Python conversions model."""

    data = models.TextField(verbose_name="input javascript object field")

    def __str__(self) -> str:
        """Human readable string representation"""
        return str(self.data)

    def __repr__(self) -> str:
        """Object string representation."""
        return "Js2PyConversion(data={})".format(repr(self.data))

    def get_python_conversion(self) -> Any:
        """Get python coversion of javascript object input data."""
        return json.loads(self.data)

    def get_prettified_python_conversion(self) -> str:
        """Get prettified string representation of converted python object."""
        return pprint.pformat(self.get_python_conversion(), indent=4)
