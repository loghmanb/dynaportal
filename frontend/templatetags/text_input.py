from django import template

from ..common import Field

register = template.Library()


@register.inclusion_tag('frontend/components/text_input.html', takes_context=True)
def text_input(context: dict, field: Field) -> dict[str, Field]:
    context['field'] = field
    return context
