# Generated by Django 5.0.3 on 2024-04-15 03:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_basicuser_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicuser',
            name='date_of_birth',
            field=models.DateField(auto_now_add=True),
        ),
    ]
