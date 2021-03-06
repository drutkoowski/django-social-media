# Generated by Django 4.0.4 on 2022-06-11 14:52

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_profile_picture'),
        ('posts', '0018_alter_story_expiration_date_alter_story_story_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 14, 52, 26, 163355)),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=100, size=[800, 600], upload_to='stories/'),
        ),
        migrations.CreateModel(
            name='StoryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.story')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
    ]
