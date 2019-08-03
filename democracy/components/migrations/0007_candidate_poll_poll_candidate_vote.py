# Generated by Django 2.2.3 on 2019-08-03 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0006_auto_20190801_0459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='pic_folder/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.SystemUser')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.SystemUser')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.Candidate')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.Poll')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.SystemUser')),
            ],
        ),
        migrations.CreateModel(
            name='Poll_Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.Candidate')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.Poll')),
            ],
        ),
    ]
