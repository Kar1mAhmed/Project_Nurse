# Generated by Django 5.0.3 on 2024-04-15 18:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_booking_nurse_remove_booking_patient'),
        ('users', '0026_alter_basicuser_address'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='nurse',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='patient',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='users.basicuser'),
            preserve_default=False,
        ),
    ]
