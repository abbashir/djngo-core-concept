from django.core.exceptions import ValidationError


def gmail_validator(value):
    if not '@gmail' in value:
        raise ValidationError("Please enter gmail address")
    return value
