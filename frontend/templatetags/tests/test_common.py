"""Module for testing common tags and filters."""
from django.test.testcases import TestCase

from ..common import item


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