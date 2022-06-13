# Generated by Django 4.0.4 on 2022-06-11 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_alter_story_expiration_date_alter_story_story_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 11, 22, 18, 100979)),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_image',
            field=models.ImageField(upload_to='stories/'),
        ),
    ]
