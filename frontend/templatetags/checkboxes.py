"""Module for InputText component."""
from django import template

from ..common import Field

register = template.Library()


@register.inclusion_tag(
        'frontend/components/checkboxes.html',
        takes_context=True)
def checkboxes(context: dict, field: Field) -> dict[str, Field]:
    """Input text tag."""
    context['field'] = field
    return context
