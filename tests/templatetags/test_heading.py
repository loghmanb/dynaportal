"""Module for testing common tags and filters."""

from dynaportal.common import Field, FieldType

from . import BaseTestCase


class FieldHeadingTestCase(BaseTestCase):
    """Field Heading test cases."""

    def setUp(self) -> None:
        """Setup."""
        self.template = "{% load heading %}" "{% heading field %}"

    def test_heading(self):
        """Test heading."""
        field = Field(
            "heading-id",
            "heading-name",
            FieldType.HEADING,
            "Foo heading",
        )
        rendered = self.render_template(self.template, {"field": field})
        self.assertEqual(
            rendered,
            '\n\n<legend class="govuk-fieldset__legend govuk-fieldset__legend--l">\n  <h1 class="govuk-label-wrapper">\n  <label class="govuk-label govuk-label--l" for="heading-id">\n    Foo heading\n  </label>\n</h1>\n</legend>\n',
        )
