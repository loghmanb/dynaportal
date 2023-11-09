"""Module for Checkboxes component."""
from django.template import Library, RequestContext

from ..common import Field

register = Library()


@register.inclusion_tag("frontend/components/checkboxes.html", takes_context=True)
def checkboxes(context: RequestContext, field: Field) -> RequestContext:
    """Checkboxes tag."""
    context["field"] = field
    return context
