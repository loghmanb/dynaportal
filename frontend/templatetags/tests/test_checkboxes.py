"""Module for testing CheckBoxes tag."""
from project.utils import BaseTestCase
from ...common import Field, FieldType


class CheckBoxesTest(BaseTestCase):
    """Check Boxes test case."""

    def setUp(self) -> None:
        """Setup."""
        self.template = (
            '{% load checkboxes %}'
            '{% checkboxes field %}'
        )

    def test_checkboxes_simple(self):
        field = Field(
            "transport-id",
            "transport",
            FieldType.CHECKBOXES,
            "Which types of waste do you transport?",
            options={
                "style-bold-size": True,
                "items": [
                    {
                        "caption": "Waste from animal carcasses", 
                        "value": "animal-carcasses",
                    },
                    {
                        "caption": "Waste from mines or quarries", 
                        "value": "mines/quarries",
                    },
                    {
                        "caption": "Farm or agricultural waste", 
                        "value": "agricultural-waste",
                    },
                ]
            },
        )
        rendered = self.render_template(self.template, {'field': field})
        self.assertEqual(rendered, '<div class="govuk-form-group ">\n    \n<fieldset class="govuk-fieldset" aria-describedby="countries-hint">\n  <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">\n    <h1 class="govuk-label-wrapper">\n  <label class="govuk-label govuk-label--l" for="transport-id">\n    Which types of waste do you transport?\n  </label>\n</h1>\n  </legend>\n  \n  \n  <div class="govuk-checkboxes " data-module="govuk-checkboxes">\n    \n    <div class="govuk-checkboxes__item">\n      <input class="govuk-checkboxes__input" id="transport-id-animal-carcasses" name="transport" type="checkbox" value="animal-carcasses">\n      <label class="govuk-label govuk-checkboxes__label" for="transport">\n        Waste from animal carcasses\n      </label>\n      \n    </div>\n    \n    <div class="govuk-checkboxes__item">\n      <input class="govuk-checkboxes__input" id="transport-id-mines/quarries" name="transport" type="checkbox" value="mines/quarries">\n      <label class="govuk-label govuk-checkboxes__label" for="transport">\n        Waste from mines or quarries\n      </label>\n      \n    </div>\n    \n    <div class="govuk-checkboxes__item">\n      <input class="govuk-checkboxes__input" id="transport-id-agricultural-waste" name="transport" type="checkbox" value="agricultural-waste">\n      <label class="govuk-label govuk-checkboxes__label" for="transport">\n        Farm or agricultural waste\n      </label>\n      \n    </div>\n    \n    \n  </div>\n</fieldset>\n\n</div>\n')
