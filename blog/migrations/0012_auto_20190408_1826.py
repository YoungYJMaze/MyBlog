# Generated by Django 2.1.8 on 2019-04-08 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190406_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='img',
            field=models.ImageField(default=None, null=None, upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default=None, null=None, upload_to='photo'),
        ),
    ]
