"""Module for testing Select tag."""

from dynaportal.common import Field, FieldType

from . import BaseTestCase


class RadiosTest(BaseTestCase):
    """Select test case."""

    def setUp(self) -> None:
        """Setup."""
        self.template = "{% load select %}{% select field %}"

    def test_select(self):
        field = Field(
            "chaged-name",
            "change-name",
            FieldType.SELECT,
            "Have you changed your name?",
            hint="This includes changing your last name or spelling your name differently.",
            options={
                "style-bold-size": True,
                "items": [
                    {
                        "caption": "Yes",
                        "value": "yes",
                    },
                    {
                        "caption": "No",
                        "value": "no",
                    },
                ],
            },
        )
        rendered = self.render_template(self.template, {"field": field})
        self.assertEqual(
            rendered,
            '<div class="govuk-form-group ">\n    \n<div class="govuk-form-group ">\n    <h1 class="govuk-label-wrapper">\n  <label class="govuk-label govuk-label--l" for="chaged-name">\n    Have you changed your name?\n  </label>\n</h1>\n    <div class="govuk-hint">This includes changing your last name or spelling your name differently.</div>\n    \n    <select class="govuk-select " name="change-name">\n      <option value="" selected>Choose an item</option>\n      <option value="yes">Yes</option>\n      <option value="no">No</option>\n    </select>\n  </div>\n\n</div>\n',
        )

    def test_select_with_error(self):
        field = Field(
            "chaged-name",
            "change-name",
            FieldType.SELECT,
            "Have you changed your name?",
            hint="This includes changing your last name or spelling your name differently.",
            error="Select an item",
            options={
                "style-bold-size": True,
                "items": [
                    {
                        "caption": "Yes",
                        "value": "yes",
                    },
                    {
                        "caption": "No",
                        "value": "no",
                    },
                ],
            },
        )
        rendered = self.render_template(self.template, {"field": field})
        self.assertEqual(
            rendered,
            '<div class="govuk-form-group govuk-form-group--error">\n    \n<div class="govuk-form-group govuk-form-group--error">\n    <h1 class="govuk-label-wrapper">\n  <label class="govuk-label govuk-label--l" for="chaged-name">\n    Have you changed your name?\n  </label>\n</h1>\n    <div class="govuk-hint">This includes changing your last name or spelling your name differently.</div>\n    <p class="govuk-error-message">\n    <span class="govuk-visually-hidden">Error:</span> Select an item\n</p>\n    <select class="govuk-select govuk-select--error" name="change-name">\n      <option value="" selected>Choose an item</option>\n      <option value="yes">Yes</option>\n      <option value="no">No</option>\n    </select>\n  </div>\n\n</div>\n',
        )
