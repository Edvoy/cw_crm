from django.db import models

from main_crm.models import Company
from phonenumber_field.modelfields import PhoneNumberField

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