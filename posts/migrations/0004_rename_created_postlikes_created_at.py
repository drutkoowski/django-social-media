# Generated by Django 4.0.4 on 2022-06-02 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_postlikes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postlikes',
            old_name='created',
            new_name='created_at',
        ),
    ]
