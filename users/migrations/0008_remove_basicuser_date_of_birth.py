# Generated by Django 5.0.3 on 2024-04-15 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_basicuser_addres_basicuser_date_of_birth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicuser',
            name='date_of_birth',
        ),
    ]