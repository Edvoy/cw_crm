# Generated by Django 3.2.2 on 2021-05-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
