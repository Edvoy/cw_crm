# Generated by Django 3.2.2 on 2021-05-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='email_id',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]