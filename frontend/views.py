from django.shortcuts import render

from .common import Field, FieldType


def home(request):
    fields = [
        Field(
            "address-line-123",
            "address-line-1",
            FieldType.INPUT_TEXT,
            "Home Address",
            question="What is your home address?",
            hint="The name you’ll use on promotional material 123",
            error="Enter an event name 123",
            options={"size":5,"input_prefix": "£", "input_suffix": "per item 123", "is_code": True, "spellchecker": False}),
        Field(
            "countries-id",
            "countries",
            FieldType.CHECKBOXES,
            "What is your nationality?",
            hint="If you have dual nationality, select all options that are relevant to you.",
            options={
                "items": ["France", "Portugal","Spain", ]
            }
        ),
    ]

    return render(request, 'frontend/home.html', context={"fields": fields, 'one_question': len(fields)==1})
