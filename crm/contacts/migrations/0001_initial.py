# Generated by Django 3.2.2 on 2021-05-19 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_first_name', models.CharField(max_length=255)),
                ('contact_last_name', models.CharField(max_length=255)),
                ('contact_job', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=45, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=45, null=True)),
                ('contact_notes', models.TextField(blank=True, null=True)),
                ('contact_created_on', models.DateTimeField(auto_now_add=True)),
                ('contact_company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
            options={
                'ordering': ['contact_last_name'],
            },
        ),
    ]
