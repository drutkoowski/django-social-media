# Generated by Django 4.0.4 on 2022-06-04 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_postcomments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcomments',
            options={'verbose_name_plural': 'Post Comments'},
        ),
    ]
