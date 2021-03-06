# Generated by Django 4.0.4 on 2022-06-10 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_profile_picture'),
        ('posts', '0007_alter_postcomments_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_image', models.ImageField(upload_to='stories/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_saved', models.BooleanField(default=False)),
                ('expiration_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
            options={
                'verbose_name_plural': 'Stories',
            },
        ),
    ]
