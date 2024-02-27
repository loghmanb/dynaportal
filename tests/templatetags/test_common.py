"""Module for testing common tags and filters."""
from django.test.testcases import TestCase
from dynaportal.templatetags.common import item

from . import BaseTestCase


class FieldLabelTestCase(BaseTestCase):
    """Field Lablel test cases."""

    def setUp(self) -> None:
        """Setup."""
        self.template = (
            '{% load common %}'
            '{% field_label id string bold %}'
        )

    def test_normal_label(self):
        """Test normal label."""
        rendered = self.render_template(
            self.template,
            {'id': 123, 'string': 'Test label', 'bold': False}
            )
        self.assertEqual(rendered, '<label class="govuk-label" for="123">\n  Test label\n</label>')

    def test_bold_label(self):
        """Test bold label."""
        rendered = self.render_template(
            self.template,
            {'id': 123, 'string': 'Test label', 'bold': True}
            )
        self.assertEqual(rendered, '<h1 class="govuk-label-wrapper">\n  <label class="govuk-label govuk-label--l" for="123">\n    Test label\n  </label>\n</h1>')

class HintTestCase(BaseTestCase):
    """Hint test cases."""

    def test_hint(self) -> None:
        """Test hint."""
        template = '{% load common %}{% hint string %}'
        rendered = self.render_template(template, {'string': 'Sample hint comes here.'})
        self.assertEqual(rendered, '<div class="govuk-hint">Sample hint comes here.</div>')


class FieldErrorTestCase(BaseTestCase):
    """Field Error test cases."""

    def test_field_error_label(self) -> None:
        """Setup."""
        template = '{% load common %}{% field_error string %}'
        rendered = self.render_template(template, {'string': 'Sample serror text comes here!'})
        self.assertEqual(rendered, '<p class="govuk-error-message">\n    <span class="govuk-visually-hidden">Error:</span> Sample serror text comes here!\n</p>')

class ItemFilterTestCase(TestCase):
    """Item filter test cases."""
    def test_if_is_not_found_in_dict_or_list(self):
        """Test if item is not found in dict or list"""
        result = item({'foo': 'bar'}, "abc")
        self.assertIsNone(result)
        result = item(['foo', 'bar'], 2)
        self.assertIsNone(result)

    def test_if_option_is_dict(self):
        """Test if option is dict."""
        result = item({'foo': 'bar'}, "foo")
        self.assertEqual(result, 'bar')

    def test_if_option_is_list(self):
        """Test if option is list."""
        result = item(['foo', 'bar'], 1)
        self.assertEqual(result, 'bar')

    def test_reurn_default_if_item_is_not_found(self):
        """Test return default value if item not found."""
        result = item({'foo': 'bar'}, "abc,efg")
        self.assertEqual(result, "efg")
        result = item(['foo', 'bar'], "2,efg")
        self.assertEqual(result, "efg")

    def test_return_default_if_options_is_none_or_empty(self):
        """Test return default value if options is none or empty."""
        result = item({}, "abc,efg")
        self.assertEqual(result, "efg")
        result = item([], "2,efg")
        self.assertEqual(result, "efg")
        result = item(None, "2,efg")
        self.assertEqual(result, "efg")

    def test_return_second_para_if_first_is_not_exist(self):
        """Test return second parameter if the first one is not exists."""
        result = item({"second": "second-val"}, "first|second,def")
        self.assertEqual(result, "second-val")
        result = item({}, "first|second,def")
        self.assertEqual(result, "def")
