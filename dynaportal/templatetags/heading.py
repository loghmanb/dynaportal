"""Module for Heading component."""

from django.template import Library, RequestContext

from ..common import Field

register = Library()


@register.inclusion_tag("dynaportal/components/heading.html", takes_context=True)
def heading(context: RequestContext, field: Field) -> RequestContext:
    """Heading tag."""
    context["field"] = field
    return context
