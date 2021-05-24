"""
setup for cron service
"""

from .gmail_api import getMail
from .models import Email

def syncMails():
    """
    sync email function to synchronize email (details on crm.settings.CRONJOBS) 
    """
    print("sync in progress")
    email_id, sender, recipient, subject, message = getMail()
    Email.objects.create(
        from_email = sender,
        to_email = recipient,
        email_subject = subject,
        email_message = message
        )
    print("sync completed")