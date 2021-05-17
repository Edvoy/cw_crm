from django.shortcuts import render, redirect
from .gmail_api import getMail
from .models import Email
from .forms import EmailForm

from contacts.models import Contact


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
    return redirect('/emails')

def deleteEmail(request, id):
    email = Email.objects.get(pk = id)
    email.delete()
    return redirect('/emails')

def listEmail(request):
    emails = Email.objects.all()
    form = EmailForm()
    context = {
        'emails' : emails,
        'form' : form,
    }
    return render(request, 'emails/index.html', context)

def filterEmailFromContact(request,id):
    email = Email.objects.filter(to_email = id)
    form = EmailForm(request.POST)
    context = {
        'emails' : email,
        'form' : form,
    }
    return render(request, 'emails/index.html', context)

def filterEmailFromCompany(request,id):
    email = Email.objects.filter(field__in=Contact.object.filter(contact_company = id))
    form = EmailForm(request.POST)
    context = {
        'emails' : email,
        'form' : form,
    }
    return render(request, 'emails/index.html', context)