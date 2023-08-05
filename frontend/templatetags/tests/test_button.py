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

    def test_button_start(self):
        rendered = self.render_template(
            self.template,
            {'label': 'Start Application', 'button_type': 'start'}
            )
        self.assertEqual(rendered, '\n<a href="#" role="button" draggable="false" class="govuk-button govuk-button--start" data-module="govuk-button">\n    Start Application\n    <svg class="govuk-button__start-icon" xmlns="http://www.w3.org/2000/svg" width="17.5" height="19" viewBox="0 0 33 40" aria-hidden="true" focusable="false">\n      <path fill="currentColor" d="M0 0h13l20 20-20 20H0l20-20z" />\n    </svg></a>\n')

    def test_button_primary(self):
        rendered = self.render_template(
            self.template,
            {'label': 'Test Button', 'button_type': 'primary'}
            )
        self.assertEqual(rendered, '\n<button class="govuk-button " data-module="govuk-button">\n    Test Button\n</button>\n')
        
    def test_button_secondary(self):
        rendered = self.render_template(
            self.template,
            {'label': 'Find address', 'button_type': 'secondary'}
            )
        self.assertEqual(rendered, '\n<button class="govuk-button govuk-button--secondary" data-module="govuk-button">\n    Find address\n</button>\n')

    def test_button_warning(self):
        rendered = self.render_template(
            self.template,
            {'label': 'Delete Application', 'button_type': 'warning'}
            )
        self.assertEqual(rendered, '\n<button class="govuk-button govuk-button--warning" data-module="govuk-button">\n    Delete Application\n</button>\n')
