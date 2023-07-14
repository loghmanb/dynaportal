"""Module for testing Text Input tag."""
from project.utils import BaseTestCase
from ...common import Field, FieldType

class InputTextTest(BaseTestCase):
    """Text Input test case."""
    def setUp(self) -> None:
        """Setup."""
        self.sample_template = (
            '{% load text_input %}'
            '{% text_input field %}'
            )

    def test_input_text_simple(self):
        """Test if version env variable is not set."""
        field = Field(
            "address-line-id",
            "address-line-name",
            FieldType.INPUT_TEXT,
            question="What is your home address?",
        )
        rendered = self.render_template(self.sample_template, {'field': field})
        self.assertEqual(rendered, '<link href="foo/bar.css?"__v__=1" rel="stylesheet">')
