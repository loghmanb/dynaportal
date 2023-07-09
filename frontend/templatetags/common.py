"""Module for common tags and filters."""
from django import template


register = template.Library()


@register.inclusion_tag('frontend/components/base_component/hint.html')
def hint(string: str):
    """Hint tag."""
    return {"hint": string, }


@register.inclusion_tag("frontend/components/base_component/field_error.html")
def field_error(string: str):
    """Field error tag."""
    return {"error": string, }


@register.filter(is_safe=True)
def item(options: dict | list, idx: int | str) -> any:
    """Item filter."""
    if options:
        if isinstance(options, dict):
            return options.get(idx)
        elif len(options) > idx:
            return options[idx]
    return None
