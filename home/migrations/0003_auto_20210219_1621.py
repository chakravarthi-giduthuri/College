# Generated by Django 3.1.6 on 2021-02-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_posts_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='files',
            field=models.FileField(default=None, upload_to='files/media/'),
        ),
    ]
