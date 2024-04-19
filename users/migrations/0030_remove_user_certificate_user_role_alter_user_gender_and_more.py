# Generated by Django 5.0.3 on 2024-04-19 03:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_user_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='certificate',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('patient', 'Patient'), ('nurse', 'Nurse')], default='patient', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Male', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='national_id',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='user',
            name='national_id_image',
            field=models.URLField(default='image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='selfie',
            field=models.URLField(default='image'),
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_image', models.URLField(default='image')),
                ('department', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='nurse', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(default='yy/mm/dd')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='BasicUser',
        ),
    ]
