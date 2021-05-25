"""
setup for cron service
"""
from django.db.models import Q
from .gmail_api import getMail
from .models import Email

from contacts.models import Contact

def syncMails():
    """
    sync email function to synchronize email (details on crm.settings.CRONJOBS) 
    """
    print("sync in progress")
    email_id, sender, recipient, subject, message = getMail()
    try:
        Email.objects.get(email_id = email_id)
    except Email.DoesNotExist :
        filter = Contact.objects.filter(Q(contact_email=sender) | Q(contact_email=recipient)).values('id')
        contact = Contact.objects.get(id=str(filter).strip('<QuerySet [{\'id\': ').strip('}]>'))
        Email.objects.create(
            email_id = email_id,
            from_email = sender, 
            contact_id = contact,
            to_email = recipient,
            email_subject = subject,
            email_message = message
            )
    print("sync completed")