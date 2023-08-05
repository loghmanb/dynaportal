"""Module for Checkboxes component."""
from django import template

from ..common import Field

register = template.Library()


@register.inclusion_tag(
        'frontend/components/radios.html',
        takes_context=True)
def radios(context: dict, field: Field) -> dict[str, Field]:
    """Radios tag."""
    context['field'] = field
    return context
