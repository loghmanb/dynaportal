"""Module for Button component."""

from typing import Dict

from django import template

register = template.Library()


@register.inclusion_tag("dynaportal/components/button.html", takes_context=True)
def button(
    context: Dict,
    label: str,
    button_type: str = "start",
    value: str = "start",
    disabled=False,
) -> Dict:
    """Button tag."""
    context["label"] = label
    context["type"] = button_type
    context["disabled"] = disabled
    context["value"] = value
    return context
