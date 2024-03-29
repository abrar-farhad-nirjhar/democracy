# Generated by Django 2.2.3 on 2019-08-01 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('components', '0005_auto_20190801_0456'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.CharField(choices=[('M', 'MANAGER'), ('R', 'REGULAR')], max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
