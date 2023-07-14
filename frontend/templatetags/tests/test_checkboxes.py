"""Module for testing CheckBoxes tag."""
from project.utils import BaseTestCase
from ...common import Field, FieldType


class CheckBoxesTest(BaseTestCase):
    """Check Boxes test case."""

    def setUp(self) -> None:
        """Setup."""
        self.sample_template = (
            '{% load checkboxes %}'
            '{% checkboxes field %}'
        )

    def test_checkboxes_simple(self):
        pass
