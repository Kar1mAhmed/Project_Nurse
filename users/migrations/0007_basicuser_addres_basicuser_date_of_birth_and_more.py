# Generated by Django 5.0.3 on 2024-04-15 03:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_basicuser_passwordresettoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicuser',
            name='addres',
            field=models.CharField(default='Egypt', max_length=100),
        ),
        migrations.AddField(
            model_name='basicuser',
            name='date_of_birth',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='basicuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='certificate',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='national_id_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='selfie',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
