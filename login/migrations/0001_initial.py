# Generated by Django 5.0.6 on 2024-05-17 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_id', models.IntegerField(verbose_name='primary_key=True')),
                ('st_password', models.CharField(max_length=15)),
            ],
        ),
    ]
