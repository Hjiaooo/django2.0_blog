# Generated by Django 2.1.1 on 2018-09-08 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180908_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
