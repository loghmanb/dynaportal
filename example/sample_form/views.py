from django.shortcuts import render

from dynaportal.common import Field, FieldType


def home(request):
    one_question = False
    fields = [
        Field(
            "chaged-name",
            "change-name",
            FieldType.SELECT,
            "Have you changed your name?",
            error="Select an item",
            hint="This includes changing your last name or spelling your name differently.",
            options={
                "style-bold-size": True,
                "inline": True,
                "items": [
                    {
                        "caption": "Yes",
                        "value": "yes",
                    },
                    {
                        "caption": "No",
                        "value": "no",
                    },
                ],
            },
        ),
        Field(
            "live-id",
            "live",
            FieldType.RADIOS,
            "Where do you live?",
            options={
                "style-bold-size": False,
                "inline": False,
                "items": [
                    {
                        "caption": "England",
                        "value": "england",
                        "hint": "You’ll have a user ID if you’ve registered for Self Assessment or filed a tax return online before.",
                    },
                    {
                        "divider": "or",
                        "caption": "Wales",
                        "value": "wales",
                        "hint": "If you don’t have a GOV.UK One Login, you can create one.",
                    },
                ],
            },
        ),
    ]
    """
        Field(
            "countries-id",
            "countries",
            FieldType.CHECKBOXES,
            "Will you be travelling to any of these countries?",
            hint="Select all countries that apply.",
            error="Sample error message comes here.",
            options={
                "style-bold-size": True,
                "items": [
                    {
                        "caption": "France",
                        "value": "fr",
                        "hint": "including French Southern and Antarctic Lands",
                    },
                    {
                        "caption": "Portugal",
                        "value": "pr",
                    },
                    {
                        "caption": "Spain",
                        "value": "sp",
                    },
                ],
                "none": "No, I will not be travelling to any of these countries",
            },
        ),
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
                "spellchecker": False,
            },
        ),
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
                "spellchecker": False,
            },
        ),
        Field("firstname", "firstname", FieldType.INPUT_TEXT, "Firstname"),
    ]
    """
    return render(
        request,
        "dynaportal/home.html",
        context={
            "action": "/",
            "tradeMark": "DynaportalExample",
            "service": {
                "title": "Trearment plan",
                "link": "/",
                "menu_items": [
                    {
                        "title": "Generate new treatment plan",
                        "active": True,
                        "link": "generate",
                    }
                ],
            },
            "banner": {
                "tag": "alpha",
                "text": "In the first phase, it is just focus on generating a treatment plan!",
            },
            "page": {
                "title": "Generate treatment plan [Dentition]",
            },
            "fields": fields,
            "one_question": one_question,
        },
    )
