# Generated by Django 3.2.2 on 2021-05-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_auto_20210514_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='sync_time',
        ),
        migrations.AlterField(
            model_name='email',
            name='receive_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
