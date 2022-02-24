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
