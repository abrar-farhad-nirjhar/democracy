# Generated by Django 2.2.3 on 2019-08-22 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0007_candidate_poll_poll_candidate_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='finished',
            field=models.CharField(default='false', max_length=10),
        ),
    ]
