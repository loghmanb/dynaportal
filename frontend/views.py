from django.shortcuts import render

from .common import Field, FieldType


def home(request):
    fields = [
        Field(
            "address-line-123",
            "address-line-1",
            FieldType.INPUT_TEXT,
            question="What is your home address?",
            size=5,
            hint="The name you’ll use on promotional material 123",
            error="Enter an event name 123",
            options={"input_prefix": "£", "input_suffix": "per item 123", "is_code": True, "spellchecker": False}),
    ]

    return render(request, 'frontend/home.html', context={"fields": fields, 'one_question': len(fields)==1})
