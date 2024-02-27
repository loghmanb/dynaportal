"""Module for testing Text Input tag."""
from dynaportal.common import Field, FieldType

from . import BaseTestCase


class InputTextTest(BaseTestCase):
    """Text Input test case."""

    def setUp(self) -> None:
        """Setup."""
        self.template = (
            '{% load text_input %}'
            '{% text_input field %}'
        )

    def test_input_text_simple(self):
        """Test if version env variable is not set."""
        field = Field(
            "address-line-id",
            "address-line-name",
            FieldType.INPUT_TEXT,
            "Home Address",
        )
        rendered = self.render_template(self.template, {'field': field})
        self.assertEqual(rendered, '<div class="govuk-form-group ">\n    \n<label class="govuk-label" for="address-line-id">\n  Home Address\n</label>\n\n\n<div class="govuk-input__wrapper">\n  \n  <input type="text" \n    class="govuk-input " \n    id="address-line-id" name="address-line-name"\n    \n    \n    >\n  \n</div>\n\n</div>\n')

    def test_input_text_if_one_question(self):
        """Test if version env variable is not set."""
        field = Field(
            "address-line-id",
            "address-line-name",
            FieldType.INPUT_TEXT,
            "What is your home address?",
        )
        rendered = self.render_template(
            self.template,
            {'field': field, 'one_question': True},
        )
        self.assertEqual(rendered, '<div class="govuk-form-group ">\n    \n<h1 class="govuk-label-wrapper">\n  <label class="govuk-label govuk-label--l" for="address-line-id">\n    What is your home address?\n  </label>\n</h1>\n\n\n<div class="govuk-input__wrapper">\n  \n  <input type="text" \n    class="govuk-input " \n    id="address-line-id" name="address-line-name"\n    \n    \n    >\n  \n</div>\n\n</div>\n')

    def test_input_text_for_post_code_with_error(self):
        """Test input text for post code with error."""
        field =  Field(
            "post-code-id",
            "post-code",
            FieldType.INPUT_TEXT,
            "Post Code",
            hint="What is the post code for your home address?",
            error="Enter a valid post code",
            options={
                "size": 7,
                "input_size": 5,
                "is_code": True,
                "spellchecker": False
                }
            )
        rendered = self.render_template(self.template, {'field': field, })
        self.assertEqual(rendered, '<div class="govuk-form-group govuk-form-group--error">\n    \n<label class="govuk-label" for="post-code-id">\n  Post Code\n</label>\n<div class="govuk-hint">What is the post code for your home address?</div>\n<p class="govuk-error-message">\n    <span class="govuk-visually-hidden">Error:</span> Enter a valid post code\n</p>\n<div class="govuk-input__wrapper">\n  \n  <input type="text" \n    class="govuk-input  govuk-input--width-5  govuk-input--error  govuk-input--extra-letter-spacing " \n    id="post-code-id" name="post-code"\n    \n    maxlength=\'7\'\n    spellcheck="false">\n  \n</div>\n\n</div>\n')

    def test_text_input_with_suffix_and_postfix(self):
        """Test text input with suffix and postfix."""
        field = Field(
            "product-amount-id",
            "product-amount",
            FieldType.INPUT_TEXT,
            "Product Amount",
            options={
                "size": 5,
                "input_prefix": "£",
                "input_suffix": "per item",
                "spellchecker": False
                }
            )
        rendered = self.render_template(self.template, {'field': field, })
        self.assertEqual(rendered, '<div class="govuk-form-group ">\n    \n<label class="govuk-label" for="product-amount-id">\n  Product Amount\n</label>\n\n\n<div class="govuk-input__wrapper">\n  \n  <div class="govuk-input__prefix" aria-hidden="true">£</div>\n  \n  <input type="text" \n    class="govuk-input  govuk-input--width-5 " \n    id="product-amount-id" name="product-amount"\n    \n    maxlength=\'5\'\n    spellcheck="false">\n  \n  <div class="govuk-input__suffix" aria-hidden="true">per item</div>\n  \n</div>\n\n</div>\n')
