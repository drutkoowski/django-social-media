# Generated by Django 4.0.4 on 2022-06-01 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfollowing',
            old_name='created',
            new_name='created_at',
        ),
    ]
