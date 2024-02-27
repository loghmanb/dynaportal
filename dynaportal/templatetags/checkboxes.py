"""Module for Checkboxes component."""

from typing import Dict

from django import template

from ..common import Field

register = template.Library()


@register.inclusion_tag("dynaportal/components/checkboxes.html", takes_context=True)
def checkboxes(context: Dict, field: Field) -> Dict[str, Field]:
    """Checkboxes tag."""
    context["field"] = field
    return context
