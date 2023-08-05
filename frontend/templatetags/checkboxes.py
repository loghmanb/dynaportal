"""Module for Checkboxes component."""
from django import template

from ..common import Field

register = template.Library()


@register.inclusion_tag(
        'frontend/components/checkboxes.html',
        takes_context=True)
def checkboxes(context: dict, field: Field) -> dict[str, Field]:
    """Checkboxes tag."""
    context['field'] = field
    return context
