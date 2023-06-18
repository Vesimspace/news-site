# Generated by Django 4.2.2 on 2023-06-14 15:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MinLengthValidator(5)]),
        ),
    ]