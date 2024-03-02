"""Module for Checkboxes component."""

from typing import List

from django.template import Library, RequestContext

from ..common import Field

register = Library()


@register.inclusion_tag("dynaportal/components/radios.html", takes_context=True)
def radios(context: RequestContext, field: Field) -> RequestContext:
    """Radios tag."""
    context["field"] = field
    return context


@register.inclusion_tag("dynaportal/components/radio_items.html", takes_context=True)
def radio_items(
    context: RequestContext, field_id: str, name: str, items: List
) -> RequestContext:
    """Radio items tag."""
    context["field_id"] = field_id
    context["name"] = name
    context["items"] = items
    return context
