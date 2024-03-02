"""Module for testing Radios tag."""

from dynaportal.common import Field, FieldType

from . import BaseTestCase


class RadiosTest(BaseTestCase):
    """Radios test case."""

    def setUp(self) -> None:
        """Setup."""
        self.template = "{% load radios %}{% radios field %}"

    def test_simple_inline_radios(self):
        field = Field(
            "chaged-name",
            "change-name",
            FieldType.RADIOS,
            "Have you changed your name?",
            hint="This includes changing your last name or spelling your name differently.",
            options={
                "style-bold-size": True,
                "inline": True,
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
            '<div class="govuk-form-group ">\n    \n<fieldset class="govuk-fieldset">\n  <legend class="govuk-fieldset__legend govuk-fieldset__legend--">\n    <h1 class="govuk-label-wrapper">\n  <label class="govuk-label govuk-label--l" for="chaged-name">\n    Have you changed your name?\n  </label>\n</h1>\n  </legend>\n  <div class="govuk-hint">This includes changing your last name or spelling your name differently.</div>\n  \n  \n  <div class="govuk-radios govuk-radios--inline" data-module="govuk-radios">\n    \n<div class="govuk-radios" data-module="govuk-radios">\n    \n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="chaged-name-yes" name="change-name" type="radio"\n            value="yes">\n        <label class="govuk-label govuk-radios__label" for="chaged-name-yes">\n            Yes\n        </label>\n        \n    </div>\n    \n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="chaged-name-no" name="change-name" type="radio"\n            value="no">\n        <label class="govuk-label govuk-radios__label" for="chaged-name-no">\n            No\n        </label>\n        \n    </div>\n    \n</div>\n\n  </div>\n  \n</fieldset>\n\n</div>\n',
        )
