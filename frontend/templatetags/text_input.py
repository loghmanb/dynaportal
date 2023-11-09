"""Module for InputText component."""
from django.template import Library, RequestContext

from ..common import Field

register = Library()


@register.inclusion_tag("frontend/components/text_input.html", takes_context=True)
def text_input(context: RequestContext, field: Field) -> RequestContext:
    """Input text tag."""
    context["field"] = field
    return context
