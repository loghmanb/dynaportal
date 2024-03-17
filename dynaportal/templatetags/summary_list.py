"""Module for Summary List component."""

from typing import Dict, List

from django import template

from dynaportal.common import Field

register = template.Library()


@register.inclusion_tag("dynaportal/components/summary_list.html", takes_context=True)
def summary_list(context: Dict, fields: List[Field]) -> Dict:
    """SummaryList tag."""
    context["fields"] = fields
    return context
