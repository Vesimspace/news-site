# Generated by Django 4.2.2 on 2023-06-14 14:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_user_appuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenter', models.CharField(max_length=250)),
                ('comment', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.article')),
            ],
        ),
    ]
