"""Module for testing Radios tag."""
from project.utils import BaseTestCase
from ...common import Field, FieldType


class RadiosTest(BaseTestCase):
    """Radios test case."""

    def setUp(self) -> None:
        """Setup."""
        self.template = (
            '{% load radios %}'
            '{% radios field %}'
        )

    def test_simple_radios(self):
        pass
