# Generated by Django 5.0.3 on 2024-04-18 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_alter_basicuser_dete_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=2, max_length=20),
            preserve_default=False,
        ),
    ]