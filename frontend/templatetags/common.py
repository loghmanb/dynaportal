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
    default_value = None
    if options:
        if isinstance(idx, str):
            args = idx.split(',')
            if len(args)>1:
                idx = args[0]
                default_value = args[1]
        if isinstance(options, dict):
            return options.get(idx, default_value)
        elif len(options) > idx:
            idx = int(idx)
            return options[idx]
    return default_value
