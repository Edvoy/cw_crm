from django.db import models
class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_adress = models.CharField(blank=True, max_length=255)
    company_zip_code = models.CharField(blank=True, max_length=100)
    company_city = models.CharField(blank=True, max_length=255)
    company_email = models.EmailField(blank=True)
    company_phone = models.CharField(blank=True, max_length=45, null=True)
    company_notes = models.TextField(blank=True,null=True)
    company_created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["company_name"]

    def __str__(self):
        return self.company_name