# Generated by Django 2.1.8 on 2019-04-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190405_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='essay',
            name='main_img',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='main_img',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
