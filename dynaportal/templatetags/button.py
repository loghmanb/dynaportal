"""Module for Button component."""
from django import template

from ..common import Field

register = template.Library()


@register.inclusion_tag(
        'dynaportal/components/button.html',
        takes_context=True)
def button(context: dict, label: str, button_type: str="start", disabled=False) -> dict:
    """Button tag."""
    context['label'] = label
    context['type'] = button_type
    context['disabled'] = disabled
    return context
