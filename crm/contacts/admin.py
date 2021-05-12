from django.contrib import admin

from .models import Contact

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

admin.site.register(Contact, ContactAdmin)