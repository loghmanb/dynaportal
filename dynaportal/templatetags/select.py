"""Module for Select component."""

from typing import Dict

from django import template

from dynaportal.common import Field

register = template.Library()


@register.inclusion_tag("dynaportal/components/select.html", takes_context=True)
def select(context: Dict, field: Field) -> Dict:
    """Select tag."""
    context["field"] = field
    return context
