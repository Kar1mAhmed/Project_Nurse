# Generated by Django 5.0.3 on 2024-04-18 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_otp_delete_passwordresettoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicuser',
            name='dete_of_birth',
            field=models.DateField(default='yy/mm/dd'),
        ),
    ]