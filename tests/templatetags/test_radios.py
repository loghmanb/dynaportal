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
            '<div class="govuk-form-group ">\n    \n<fieldset class="govuk-fieldset">\n  <legend class="govuk-fieldset__legend govuk-fieldset__legend--">\n    <h1 class="govuk-label-wrapper">\n  <label class="govuk-label govuk-label--l" for="chaged-name">\n    Have you changed your name?\n  </label>\n</h1>\n  </legend>\n  <div class="govuk-hint">This includes changing your last name or spelling your name differently.</div>\n  \n  \n  <div class="govuk-radios govuk-radios--inline" data-module="govuk-radios">\n     \n<div class="govuk-radios" data-module="govuk-radios">\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="chaged-name-yes" name="change-name_yes" type="radio"\n            value="yes">\n        <label class="govuk-label govuk-radios__label" for="chaged-name-yes">\n            Yes\n        </label>\n        \n    </div>\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="chaged-name-no" name="change-name_no" type="radio"\n            value="no">\n        <label class="govuk-label govuk-radios__label" for="chaged-name-no">\n            No\n        </label>\n        \n    </div>\n    \n</div>\n\n  </div>\n  \n</fieldset>\n\n</div>\n',
        )

    def test_simple_radios_with_legond(self):
        field = Field(
            "live-id",
            "live",
            FieldType.RADIOS,
            "Where do you live?",
            options={
                "style-bold-size": True,
                "items": [
                    {
                        "caption": "England",
                        "value": "england",
                    },
                    {
                        "caption": "Scotland",
                        "value": "scotland",
                    },
                    {
                        "caption": "Wales",
                        "value": "wales",
                    },
                    {
                        "caption": "Northern Ireland",
                        "value": "northen-ireland",
                    },
                ],
            },
        )
        rendered = self.render_template(self.template, {"field": field})
        self.assertEqual(
            rendered,
            '<div class="govuk-form-group ">\n    \n<fieldset class="govuk-fieldset">\n  <legend class="govuk-fieldset__legend govuk-fieldset__legend--">\n    <h1 class="govuk-label-wrapper">\n  <label class="govuk-label govuk-label--l" for="live-id">\n    Where do you live?\n  </label>\n</h1>\n  </legend>\n  \n  \n  \n   \n<div class="govuk-radios" data-module="govuk-radios">\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="live-id-england" name="live_england" type="radio"\n            value="england">\n        <label class="govuk-label govuk-radios__label" for="live-id-england">\n            England\n        </label>\n        \n    </div>\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="live-id-scotland" name="live_scotland" type="radio"\n            value="scotland">\n        <label class="govuk-label govuk-radios__label" for="live-id-scotland">\n            Scotland\n        </label>\n        \n    </div>\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="live-id-wales" name="live_wales" type="radio"\n            value="wales">\n        <label class="govuk-label govuk-radios__label" for="live-id-wales">\n            Wales\n        </label>\n        \n    </div>\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="live-id-northen-ireland" name="live_northen-ireland" type="radio"\n            value="northen-ireland">\n        <label class="govuk-label govuk-radios__label" for="live-id-northen-ireland">\n            Northern Ireland\n        </label>\n        \n    </div>\n    \n</div>\n\n  \n</fieldset>\n\n</div>\n',
        )

    def test_simple_radios_without_legond(self):
        field = Field(
            "live-id",
            "live",
            FieldType.RADIOS,
            "Where do you live?",
            options={
                "style-bold-size": False,
                "items": [
                    {
                        "caption": "England",
                        "value": "england",
                    },
                    {
                        "caption": "Scotland",
                        "value": "scotland",
                    },
                    {
                        "caption": "Wales",
                        "value": "wales",
                    },
                    {
                        "caption": "Northern Ireland",
                        "value": "northen-ireland",
                    },
                ],
            },
        )
        rendered = self.render_template(self.template, {"field": field})
        self.assertEqual(
            rendered,
            '<div class="govuk-form-group ">\n    \n<fieldset class="govuk-fieldset">\n  <legend class="govuk-fieldset__legend govuk-fieldset__legend--">\n    <label class="govuk-label" for="live-id">\n  Where do you live?\n</label>\n  </legend>\n  \n  \n  \n   \n<div class="govuk-radios" data-module="govuk-radios">\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="live-id-england" name="live_england" type="radio"\n            value="england">\n        <label class="govuk-label govuk-radios__label" for="live-id-england">\n            England\n        </label>\n        \n    </div>\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="live-id-scotland" name="live_scotland" type="radio"\n            value="scotland">\n        <label class="govuk-label govuk-radios__label" for="live-id-scotland">\n            Scotland\n        </label>\n        \n    </div>\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="live-id-wales" name="live_wales" type="radio"\n            value="wales">\n        <label class="govuk-label govuk-radios__label" for="live-id-wales">\n            Wales\n        </label>\n        \n    </div>\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="live-id-northen-ireland" name="live_northen-ireland" type="radio"\n            value="northen-ireland">\n        <label class="govuk-label govuk-radios__label" for="live-id-northen-ireland">\n            Northern Ireland\n        </label>\n        \n    </div>\n    \n</div>\n\n  \n</fieldset>\n\n</div>\n',
        )

    def test_radios_with_divider(self):
        field = Field(
            "live-id",
            "live",
            FieldType.RADIOS,
            "Where do you live?",
            options={
                "style-bold-size": False,
                "items": [
                    {
                        "caption": "England",
                        "value": "england",
                    },
                    {
                        "caption": "Scotland",
                        "value": "scotland",
                    },
                    {
                        "caption": "Wales",
                        "value": "wales",
                    },
                    {
                        "caption": "Northern Ireland",
                        "value": "northen-ireland",
                    },
                    {
                        "divider": "or",
                        "caption": "I am a British citizen living abroad",
                        "value": "abroad",
                    },
                ],
            },
        )
        rendered = self.render_template(self.template, {"field": field})
        self.assertEqual(
            rendered,
            '<div class="govuk-form-group ">\n    \n<fieldset class="govuk-fieldset">\n  <legend class="govuk-fieldset__legend govuk-fieldset__legend--">\n    <label class="govuk-label" for="live-id">\n  Where do you live?\n</label>\n  </legend>\n  \n  \n  \n   \n<div class="govuk-radios" data-module="govuk-radios">\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="live-id-england" name="live_england" type="radio"\n            value="england">\n        <label class="govuk-label govuk-radios__label" for="live-id-england">\n            England\n        </label>\n        \n    </div>\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="live-id-scotland" name="live_scotland" type="radio"\n            value="scotland">\n        <label class="govuk-label govuk-radios__label" for="live-id-scotland">\n            Scotland\n        </label>\n        \n    </div>\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="live-id-wales" name="live_wales" type="radio"\n            value="wales">\n        <label class="govuk-label govuk-radios__label" for="live-id-wales">\n            Wales\n        </label>\n        \n    </div>\n    <div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="live-id-northen-ireland" name="live_northen-ireland" type="radio"\n            value="northen-ireland">\n        <label class="govuk-label govuk-radios__label" for="live-id-northen-ireland">\n            Northern Ireland\n        </label>\n        \n    </div>\n    \n    <div class="govuk-radios__divider">or</div>\n<div class="govuk-radios__item">\n        <input class="govuk-radios__input" id="live-id-abroad" name="live_abroad" type="radio"\n            value="abroad">\n        <label class="govuk-label govuk-radios__label" for="live-id-abroad">\n            I am a British citizen living abroad\n        </label>\n        \n    </div>\n    \n</div>\n\n  \n</fieldset>\n\n</div>\n',
        )
