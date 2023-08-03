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

    def test_checkbox_small(self):
        field = Field(
            "transport-id",
            "transport",
            FieldType.CHECKBOXES,
            "Which types of waste do you transport?",
            options={
                "style-bold-size": False,
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
        self.assertEqual(rendered, '<div class="govuk-form-group ">\n    \n<fieldset class="govuk-fieldset" aria-describedby="countries-hint">\n  <legend class="govuk-fieldset__legend govuk-fieldset__legend--m">\n    <label class="govuk-label" for="transport-id">\n  Which types of waste do you transport?\n</label>\n  </legend>\n  \n  \n  <div class="govuk-checkboxes govuk-checkboxes--small" data-module="govuk-checkboxes">\n    \n    <div class="govuk-checkboxes__item">\n      <input class="govuk-checkboxes__input" id="transport-id-animal-carcasses" name="transport" type="checkbox" value="animal-carcasses">\n      <label class="govuk-label govuk-checkboxes__label" for="transport">\n        Waste from animal carcasses\n      </label>\n      \n    </div>\n    \n    <div class="govuk-checkboxes__item">\n      <input class="govuk-checkboxes__input" id="transport-id-mines/quarries" name="transport" type="checkbox" value="mines/quarries">\n      <label class="govuk-label govuk-checkboxes__label" for="transport">\n        Waste from mines or quarries\n      </label>\n      \n    </div>\n    \n    <div class="govuk-checkboxes__item">\n      <input class="govuk-checkboxes__input" id="transport-id-agricultural-waste" name="transport" type="checkbox" value="agricultural-waste">\n      <label class="govuk-label govuk-checkboxes__label" for="transport">\n        Farm or agricultural waste\n      </label>\n      \n    </div>\n    \n    \n  </div>\n</fieldset>\n\n</div>\n')

    def test_checkbox_error(self):
        field = Field(
            "countries-id",
            "countries",
            FieldType.CHECKBOXES,
            "Will you be travelling to any of these countries?",
            hint="Select all countries that apply.",
            error="Sample error message comes here.",
            options={
                "style-bold-size": True,
                "items": [
                    {
                        "caption": "France", 
                        "value": "fr",
                        "hint": "including French Southern and Antarctic Lands"
                    },
                    {
                        "caption": "Portugal",
                        "value": "pr",
                    },
                    {
                        "caption": "Spain",
                        "value": "sp",
                    }],
                "none": "No, I will not be travelling to any of these countries",
            }
        )
        rendered = self.render_template(self.template, {'field': field})
        self.assertEqual(rendered, '<div class="govuk-form-group govuk-form-group--error">\n    \n<fieldset class="govuk-fieldset" aria-describedby="countries-hint">\n  <legend class="govuk-fieldset__legend govuk-fieldset__legend--l">\n    <h1 class="govuk-label-wrapper">\n  <label class="govuk-label govuk-label--l" for="countries-id">\n    Will you be travelling to any of these countries?\n  </label>\n</h1>\n  </legend>\n  <div class="govuk-hint">Select all countries that apply.</div>\n  <p class="govuk-error-message">\n    <span class="govuk-visually-hidden">Error:</span> Sample error message comes here.\n</p>\n  <div class="govuk-checkboxes " data-module="govuk-checkboxes">\n    \n    <div class="govuk-checkboxes__item">\n      <input class="govuk-checkboxes__input" id="countries-id-fr" name="countries" type="checkbox" value="fr">\n      <label class="govuk-label govuk-checkboxes__label" for="countries">\n        France\n      </label>\n      \n      <div id="nationality-item-hint" class="govuk-hint govuk-checkboxes__hint">\n        including French Southern and Antarctic Lands\n      </div>\n      \n    </div>\n    \n    <div class="govuk-checkboxes__item">\n      <input class="govuk-checkboxes__input" id="countries-id-pr" name="countries" type="checkbox" value="pr">\n      <label class="govuk-label govuk-checkboxes__label" for="countries">\n        Portugal\n      </label>\n      \n    </div>\n    \n    <div class="govuk-checkboxes__item">\n      <input class="govuk-checkboxes__input" id="countries-id-sp" name="countries" type="checkbox" value="sp">\n      <label class="govuk-label govuk-checkboxes__label" for="countries">\n        Spain\n      </label>\n      \n    </div>\n    \n    \n    <div class="govuk-checkboxes__divider">or</div>\n    <div class="govuk-checkboxes__item">\n      <input class="govuk-checkboxes__input" id="countries-id-none" name="countries" type="checkbox" value="none" data-behaviour="exclusive">\n      <label class="govuk-label govuk-checkboxes__label" for="countries-id-none">\n        No, I will not be travelling to any of these countries\n      </label>\n    </div>\n    \n  </div>\n</fieldset>\n\n</div>\n')
