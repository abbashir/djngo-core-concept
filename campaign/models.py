from django.db import models
from django.utils.text import slugify

from .validators import gmail_validator

GENDER_CHOICES = [
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('others', 'OTHERS')
]


# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=100, verbose_name='Person Name')
    slug = models.SlugField(null=True, blank=True)
    email = models.EmailField(max_length=100, validators=[gmail_validator])
    phone = models.CharField(max_length=100, verbose_name='Mobile No', unique=True,
                             error_messages={'unique': 'Please enter unique mobile no!'},
                             help_text='Please enter no with country code')
    Gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    confirmation = models.BooleanField(verbose_name='I agree term & condition')
    published_date = models.DateField(auto_now=False, auto_now_add=False)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Campaign, self).save(*args, **kwargs)

    def __str__(self):
        return self.name  # you can use smart_text method
