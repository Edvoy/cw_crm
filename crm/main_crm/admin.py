from django.contrib import admin

from .models import Company, Contact, Email

class CompanyAdmin(admin.ModelAdmin):
    fields = [
        'company_name',
        'company_adress',
        'company_zip_code',
        'company_city',
        'company_email',
        'company_phone',
        'company_notes',
     ]

class ContactAdmin(admin.ModelAdmin):
    fields = [
        'company_name',
        'company_adress',
        'company_zip_code',
        'company_city',
        'company_email',
        'company_phone',
        'company_notes',
     ]

class EmailAdmin(admin.ModelAdmin):
    fields = [
        'from_email',
        'to_email',
        'email_subject',
        'email_message',
        'receive_time',
     ]

admin.site.register(Company, CompanyAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Email, EmailAdmin)