# Generated by Django 3.1.6 on 2021-02-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_posts_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='files/media/'),
        ),
    ]
