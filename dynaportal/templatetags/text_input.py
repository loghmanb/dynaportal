"""Module for InputText component."""

from typing import Dict

from django import template

from ..common import Field

register = template.Library()


@register.inclusion_tag("dynaportal/components/text_input.html", takes_context=True)
def text_input(context: Dict, field: Field) -> Dict[str, Field]:
    """Input text tag."""
    context["field"] = field
    return context
