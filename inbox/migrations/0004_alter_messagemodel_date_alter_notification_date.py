# Generated by Django 4.0.4 on 2022-06-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0003_remove_notification_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]