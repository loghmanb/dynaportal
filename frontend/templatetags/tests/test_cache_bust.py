"""Module for teting Cache Bust tag."""
import os

from project.utils import BaseTestCase


class CacheBustTest(BaseTestCase):
    """Cache Bust test case."""
    def setUp(self) -> None:
        """Setup."""
        self.sample_template = (
            '{% load cache_bust %}'
            '<link href="foo/bar.css?"{% cache_bust %}" rel="stylesheet">'
            )

    def test_if_verion_not_set(self):
        """Test if version env variable is not set."""
        rendered = self.render_template(self.sample_template)
        self.assertEqual(rendered, '<link href="foo/bar.css?"__v__=1" rel="stylesheet">')

    def test_if_version_has_been_set(self):
        """Test if version env variable is set."""
        os.environ["PROJECT_VERSION"] = "123"
        rendered = self.render_template(self.sample_template)
        self.assertEqual(rendered, '<link href="foo/bar.css?"__v__=123" rel="stylesheet">')
