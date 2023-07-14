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
def item(options: dict | list, idx: int | str, default_value=None) -> any:
    """Item filter."""
    default_value = None
    if isinstance(idx, str):
        args: int| list(str) = idx.split(',')
        if len(args)>1:
            idx = args[0]
            default_value = args[1]
        if isinstance(options, list):
            idx = int(idx)
        else:
            args = idx.split('|')
            if len(args)<2:
                args.append(None)

    if options:
        if isinstance(options, dict):
            return options.get(args[0], options.get(args[1], default_value))
        elif len(options) > idx:
            return options[idx]
    return default_value
