from django.shortcuts import render, redirect
from emails.gmail_api import getMail
from contacts.models import Contact
from .models import Email
from .forms import EmailForm


def syncMails():
    sender, recipient, subject, message = getMail()
    Email.objects.create(from_email = sender, to_email = recipient, email_subject = subject, email_message = message)
    return redirect('/')

#todo: comprendre pourquoi la supression n'est pas définitive
def deleteEmail(request,id):
    email = Email.objects.get(pk = id)
    email.delete()
    return redirect('/')

def listEmail(request):
    emails = Email.objects.all()
    form = EmailForm()
    context = {
        'emails' : emails,
        'form' : form,
    }
    return render(request, 'emails/index.html', context)

def filterEmail(request,id):
    print(id)
    email = Email.objects.filter(to_email = id)
    form = EmailForm(request.POST)
    context = {
        'email' : email,
        'form' : form,
    }
    return render(request, 'emails/index.html', context)