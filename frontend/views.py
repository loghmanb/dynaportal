from django.shortcuts import render

from .common import Field, FieldType


def home(request):
    one_question = False
    fields = [
         Field(
            "address-line-id",
            "address-line-name",
            FieldType.INPUT_TEXT,
            one_question and "What is your home address?" or "Home Address",
        ),
        Field(
            "post-code-id",
            "post-code",
            FieldType.INPUT_TEXT,
            "Post Code",
            hint="What is the post code for your home address?",
            error="Enter a valid post code",
            options={
                "size": 7,
                "input_size": 5,
                "is_code": True,
                "spellchecker": False
                }),
        Field(
            "address-line-123",
            "address-line-1",
            FieldType.INPUT_TEXT,
            one_question and "What is your home address?" or "Weight, in kilograms",
            hint="What is the name of the event?",
            error="Enter an event name 123",
            options={
                "size": 5,
                "input_prefix": "£",
                "input_suffix": "per item 123",
                "is_code": True,
                "spellchecker": False
                }),
    ]

    return render(request, 'frontend/home.html', context={"fields": fields, 'one_question': one_question})
