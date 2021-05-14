from django.contrib import admin
from .models import Email

class EmailAdmin(admin.ModelAdmin):
    fields = [
        'from_email',
        'to_email',
        'email_subject',
        'email_message',
     ]

admin.site.register(Email, EmailAdmin)