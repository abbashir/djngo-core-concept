from django import forms
from .models import PostModel


class postCreateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = {
            'title',
            'content'
        }


BIRTH_YEAR_CHOICES = [x for x in range(1990, 2031)]
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
CHOICES_GENDER = [('male', 'MALE'), ('female', 'FEMALE')]
CHOICES_BRAND = [('novo', 'NOVO'), ('air', 'AIR')]


class MyForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=3)
    email = forms.EmailField()
    phone = forms.CharField(required=False, initial='017')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    url = forms.URLField()
    favorite_colors = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
    Gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES_GENDER)
    Brand = forms.CharField(widget=forms.Select(choices=CHOICES_BRAND))

    Agree = forms.BooleanField()

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("write your message minimum 10 character")
