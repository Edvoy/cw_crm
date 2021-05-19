from django.shortcuts import render, redirect
from django.db.models import Q
from .gmail_api import getMail
from .models import Email
from .forms import EmailForm

from contacts.models import Contact


def syncMailsWhenUpdateContact():
    """
    when user update a contact, and click on update button in contact tab
    this function resynchronize user's mailbox
    """
    print("sync in progress")
    sender, recipient, subject, message = getMail()
    filter = Contact.objects.filter(
        Q(contact_email=sender) | Q(contact_email=recipient)
        ).values('id')
    contact = Contact.objects.get(id=str(filter).strip('<QuerySet [{\'id\': ').strip('}]>'))
    Email.objects.create(
        contact_id = contact,
        from_email = sender,
        to_email = recipient,
        email_subject = subject,
        email_message = message
        )
    print("sync completed")
    return redirect('/contact')

def syncMailsWhenUpdateCompany():
    """
    when user update a company, and click on update button in company tab
    this function resynchronize user's mailbox
    """
    print("sync in progress")
    sender, recipient, subject, message = getMail()
    filter = Contact.objects.filter(
        Q(contact_email=sender) | Q(contact_email=recipient)
        ).values('id')
    contact = Contact.objects.get(id=str(filter).strip('<QuerySet [{\'id\': ').strip('}]>'))
    Email.objects.create(
        from_email = sender, 
        contact_id = contact,
        
        to_email = recipient,
        email_subject = subject,
        email_message = message
        )
    print("sync completed")
    return redirect('/companies')

def deleteEmail(request, id):   
    """
    Delete email with delete button on email card in email tab
    """

    email = Email.objects.get(pk = id)
    email.delete()
    return redirect('/emails')

def listEmail(request):
    """
    Display all emails in email tab
    """
    emails = Email.objects.all()
    form = EmailForm()
    context = {
        'emails' : emails,
        'form' : form,
    }
    return render(request, 'emails/index.html', context)

def filterEmailFromContact(request,id):
    """
    Email filter when user click on filter button in contact tab
    Emails are filter by contact and display all communication with this contact and user
    """
    email = Email.objects.filter(contact_id = id)
    form = EmailForm(request.POST)
    context = {
        'emails' : email,
        'form' : form,
    }
    return render(request, 'emails/index.html', context)

def filterEmailFromCompany(request,id):
    """
    Email filter when user click on filter button in company tab
    Emails are filter by company and display all communication
    with this company contact and user
    """
    email = Email.objects.filter(
        contact_id__in=Contact.objects.filter(
            contact_company = id
            )
        )
    form = EmailForm(request.POST)
    context = {
        'emails' : email,
        'form' : form,
    }
    return render(request, 'emails/index.html', context)