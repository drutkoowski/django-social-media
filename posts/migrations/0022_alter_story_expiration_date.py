# Generated by Django 4.0.4 on 2022-06-12 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_alter_storycategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 13, 16, 43, 15, 478167)),
        ),
    ]
