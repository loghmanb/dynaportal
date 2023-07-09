from django import template


register = template.Library()


@register.inclusion_tag('frontend/components/hint.html')
def hint(string: str):
    return {"hint": string, }


@register.inclusion_tag("frontend/components/field_error.html")
def field_error(string: str):
    return {"error": string, }


@register.filter(is_safe=True)
def item(options: dict | list, idx: int | str) -> any:
    if options:
        if isinstance(options, dict):
            return options.get(idx)
        elif len(options) > idx:
            return options[idx]
    return None
