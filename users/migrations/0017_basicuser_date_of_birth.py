# Generated by Django 5.0.3 on 2024-04-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_basicuser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicuser',
            name='date_of_birth',
            field=models.DateField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
