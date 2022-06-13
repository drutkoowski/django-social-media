# Generated by Django 4.0.4 on 2022-06-11 15:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_alter_story_expiration_date_alter_story_story_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storycategory',
            name='story',
        ),
        migrations.AddField(
            model_name='story',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.storycategory'),
        ),
        migrations.AlterField(
            model_name='story',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 15, 13, 52, 503823)),
        ),
    ]
