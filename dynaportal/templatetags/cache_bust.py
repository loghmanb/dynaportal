"""Module providingFunction cache bust."""
import os
import uuid
from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag(name='cache_bust')
def cache_bust() -> str:
    """
    Function making cache bust.
    Ref: https://stackoverflow.com/questions/27911070/django-wont-refresh-staticfiles
    """
    if settings.DEBUG:
        version = uuid.uuid1()
    else:
        version = os.environ.get('PROJECT_VERSION')
        if version is None:
            version = '1'

    return f'__v__={version}'
