from .gmail_api import getMail
from .models import Email

def syncMails():
    print("sync in progress")
    sender, recipient, subject, message = getMail()
    Email.objects.create(
        from_email = sender,
        to_email = recipient,
        email_subject = subject,
        email_message = message
        )
    print("sync completed")