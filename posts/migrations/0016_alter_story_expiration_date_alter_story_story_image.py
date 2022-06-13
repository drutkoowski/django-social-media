# Generated by Django 4.0.4 on 2022-06-11 11:26

import datetime
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_alter_story_expiration_date_alter_story_story_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 11, 26, 48, 510036)),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=90, size=[1920, 1080], upload_to='stories/'),
        ),
    ]
