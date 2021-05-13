# Generated by Django 3.2.2 on 2021-05-13 12:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_adress', models.CharField(blank=True, max_length=255)),
                ('company_zip_code', models.CharField(blank=True, max_length=100)),
                ('company_city', models.CharField(blank=True, max_length=255)),
                ('company_email', models.EmailField(blank=True, max_length=254)),
                ('company_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('company_notes', models.TextField(blank=True, null=True)),
                ('company_created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['company_name'],
            },
        ),
    ]