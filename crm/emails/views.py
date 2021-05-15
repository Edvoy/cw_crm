from django.shortcuts import render, redirect
from emails.gmail_api import getMail
from .models import Email
from .forms import EmailForm


def syncMails():
    sender, recipient, subject, message = getMail()
    Email.objects.create(from_email = sender, to_email = recipient, email_subject = subject, email_message = message)
    return redirect('/')

def delMails(id):
    Email.objects.get(pk = id).delete()
    return redirect('/')

def listEmail(request):
    emails = Email.objects.all()
    form = EmailForm()
    syncMails()
    context = {
        'emails' : emails,
        'form' : form,
    }
    return render(request, 'emails/index.html', context)

def filterEmail(request,id):
    email = Email.objects.filter(contact_company = id)
    form = EmailForm(request.POST)
    context = {
        'email' : email,
        'form' : form,
    }
    return render(request, 'emails/index.html', context)