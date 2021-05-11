from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_adress = models.CharField(blank=True, max_length=255)
    company_zip_code = models.IntegerField(blank=True)
    company_city = models.CharField(blank=True, max_length=255)
    company_email = models.EmailField(blank=True, unique=True)
    company_phone = PhoneNumberField(blank=True)
    company_notes = models.TextField(blank=True,null=True)
    company_created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["company_name"]

    def __str__(self):
        return self.company_name


class Contact(models.Model):
    contact_first_name = models.CharField(max_length=255)
    contact_last_name = models.CharField(max_length=255)
    contact_company = models.ForeignKey('Company', on_delete=models.CASCADE,)
    contact_job = models.CharField(blank=True, max_length=255)
    contact_email = models.EmailField(unique=True)
    contact_phone = PhoneNumberField(blank=True)
    contact_notes = models.TextField(blank=True, null=True)
    contact_created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["contact_last_name"]

    def __str__(self):
        return self.contact_last_name


class Email(models.Model):
    from_email = models.ForeignKey('Contact', on_delete=models.CASCADE,)
    to_email = models.EmailField(max_length=200)
    email_subject = models.CharField(max_length=200)
    email_message = models.CharField(max_length=200)
    receive_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["receive_time"]

    def __str__(self):
        return self.receive_time