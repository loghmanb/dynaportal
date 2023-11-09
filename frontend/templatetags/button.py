"""Module for Button component."""
from django.template import Library, RequestContext


register = Library()


@register.inclusion_tag("frontend/components/button.html", takes_context=True)
def button(
    context: RequestContext, label: str, button_type: str = "start", disabled=False
) -> RequestContext:
    """Button tag."""
    context["label"] = label
    context["type"] = button_type
    context["disabled"] = disabled
    return context
