from django.template import Context, Template
from django.test.testcases import TestCase


class BaseTestCase(TestCase):
    def render_template(self, string: str, context=None):
        context = context or {}
        context = Context(context)
        return Template(string).render(context)
