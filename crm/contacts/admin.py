from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    fields = [
        'contact_first_name',
        'contact_last_name',
        'contact_company',
        'contact_job',
        'contact_email',
        'contact_phone',
        'contact_notes',
     ]

admin.site.register(Contact, ContactAdmin)