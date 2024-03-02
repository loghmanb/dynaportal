"""Module for testing Radios tag."""

from dynaportal.common import Field, FieldType

from . import BaseTestCase


class RadiosTest(BaseTestCase):
    """Radios test case."""

    def setUp(self) -> None:
        """Setup."""
        self.template = "{% load radios %}{% radios field %}"

    def test_simple_radios(self):
        pass
