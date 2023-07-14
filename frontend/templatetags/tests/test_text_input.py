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
        self.assertEqual(rendered, '<div class="govuk-form-group ">\n    \n\n<label class="govuk-label" for="address-line-id">\n  \n</label>\n\n\n\n\n\n<div class="govuk-input__wrapper">\n  \n  <input type="text" \n    class="govuk-input  govuk-input--width-None " \n    id="address-line-id" name="address-line-name"  autocomplete="None"\n    maxlength=""\n    spellcheck="">\n  \n</div>\n\n</div>\n')

    def test_input_text_if_one_question(self):
        """Test if version env variable is not set."""
        field = Field(
            "address-line-id",
            "address-line-name",
            FieldType.INPUT_TEXT,
            question="What is your home address?",
        )
        rendered = self.render_template(
            self.sample_template,
            {'field': field, 'one_question': True},
        )
        self.assertEqual(rendered, '<div class="govuk-form-group ">\n    \n\n<h1 class="govuk-label-wrapper">\n  <label class="govuk-label govuk-label--l" for="address-line-id">\n    What is your home address?\n  </label>\n</h1>\n\n\n\n\n\n<div class="govuk-input__wrapper">\n  \n  <input type="text" \n    class="govuk-input  govuk-input--width-None " \n    id="address-line-id" name="address-line-name"  autocomplete="None"\n    maxlength=""\n    spellcheck="">\n  \n</div>\n\n</div>\n')
