# Generated by Django 3.1.4 on 2021-01-30 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_auto_20210130_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
