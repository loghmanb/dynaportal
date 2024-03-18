"""Module for testing Radios tag."""

from dynaportal.common import Field, FieldType

from . import BaseTestCase


class SummaryListTest(BaseTestCase):
    """Radios test case."""

    def setUp(self) -> None:
        """Setup."""
        self.template = "{% load summary_list %}{% summary_list fields %}"

    def test_summary_list(self):
        fields = [
            Field(
                "chaged-name-radios",
                "change-name",
                FieldType.RADIOS,
                "Have you changed your name?",
                value="yes",
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
            ),
            Field(
                "chaged-name-select",
                "change-name_select",
                FieldType.SELECT,
                "Have you changed your name? (select)",
                hint="This includes changing your last name or spelling your name differently.",
                value="no",
                options={
                    "style-bold-size": True,
                    "items": [
                        {
                            "caption": "Yes, I do",
                            "value": "yes",
                        },
                        {
                            "caption": "No, I don't",
                            "value": "no",
                        },
                    ],
                },
            ),
            Field(
                "product-amount-id",
                "product-amount",
                FieldType.INPUT_TEXT,
                "Product Amount",
                value="123",
                options={
                    "size": 5,
                    "input_prefix": "£",
                    "input_suffix": "per item",
                    "spellchecker": False,
                },
            ),
        ]
        rendered = self.render_template(self.template, {"fields": fields})
        self.assertEqual(
            rendered,
            '\n<script>\nfunction change_selected_field(field) {\ndebugger;\ndocument.getElementsByName(\'selected_field\')[0].value = field;\ndocument.getElementsByTagName(\'form\')[0].submit();\n}\n</script>\n<dl class="govuk-summary-list">\n<input name="selected_field" type="hidden">\n<input name="field_values" type="hidden" value="{&quot;change-name&quot;: &quot;yes&quot;, &quot;change-name_select&quot;: &quot;no&quot;, &quot;product-amount&quot;: &quot;123&quot;}">\n  \n    <div class="govuk-summary-list__row">\n      <dt class="govuk-summary-list__key">Have you changed your name?</dt>\n      <dd class="govuk-summary-list__value">Yes</dd>\n      <dd class="govuk-summary-list__actions">\n          <a class="govuk-link" href="#" onclick="change_selected_field(\'change-name\')">Change<span class="govuk-visually-hidden"> field.caption</span></a>\n      </dd>\n    </div>\n  \n    <div class="govuk-summary-list__row">\n      <dt class="govuk-summary-list__key">Have you changed your name? (select)</dt>\n      <dd class="govuk-summary-list__value">No, I don&#x27;t</dd>\n      <dd class="govuk-summary-list__actions">\n          <a class="govuk-link" href="#" onclick="change_selected_field(\'change-name_select\')">Change<span class="govuk-visually-hidden"> field.caption</span></a>\n      </dd>\n    </div>\n  \n    <div class="govuk-summary-list__row">\n      <dt class="govuk-summary-list__key">Product Amount</dt>\n      <dd class="govuk-summary-list__value">123</dd>\n      <dd class="govuk-summary-list__actions">\n          <a class="govuk-link" href="#" onclick="change_selected_field(\'product-amount\')">Change<span class="govuk-visually-hidden"> field.caption</span></a>\n      </dd>\n    </div>\n  \n</dl>',
        )
