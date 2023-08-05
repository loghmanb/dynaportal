"""Module for testing Button tag."""
from project.utils import BaseTestCase


class ButtonTest(BaseTestCase):
    """Button test case."""

    def setUp(self) -> None:
        """Setup."""
        self.template = (
            '{% load button %}'
            '{% button label button_type %}'
        )

    def test_button_primary(self):
        rendered = self.render_template(
            self.template, 
            {'label': 'Test Button', 'button_type': 'primary'}
            )
        self.assertEqual(rendered, '\n<button class="govuk-button" data-module="govuk-button">\n    Test Button\n</button>\n')

    def test_button_start(self):
        rendered = self.render_template(
            self.template, 
            {'label': 'Test Button', 'Start Application': 'start'}
            )
        self.assertEqual(rendered, '\n<button class="govuk-button" data-module="govuk-button">\n    Test Button\n</button>\n')
