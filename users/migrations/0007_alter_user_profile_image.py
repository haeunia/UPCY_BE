# Generated by Django 4.0 on 2024-01-10 11:45

from django.db import migrations, models

import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='user_profile_image.png', null=True, upload_to=users.models.get_upload_path),
        ),
    ]
