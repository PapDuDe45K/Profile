# Generated by Django 5.1 on 2024-08-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_rename_profile_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics/'),
        ),
    ]
