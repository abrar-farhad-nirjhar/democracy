# Generated by Django 2.2.3 on 2019-07-31 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
