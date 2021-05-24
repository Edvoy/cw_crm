from django.contrib import admin
from .models import Email

class EmailAdmin(admin.ModelAdmin):
    fields = [
        'email_id',
        'contact_id',
        'from_email',
        'to_email',
        'email_subject',
        'email_message',
     ]

admin.site.register(Email, EmailAdmin)