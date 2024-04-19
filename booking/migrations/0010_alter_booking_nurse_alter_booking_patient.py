# Generated by Django 5.0.3 on 2024-04-19 04:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_alter_booking_nurse_alter_booking_patient'),
        ('users', '0030_remove_user_certificate_user_role_alter_user_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='nurse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nurse_bookings', to='users.nurse'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_bookings', to='users.patient'),
        ),
    ]
