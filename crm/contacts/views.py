from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


def listContact(request):
    contacts = Contact.objects.all()
    form = ContactForm()
    context = {
        'contacts' : contacts,
        'form' : form
    }
    return render(request, 'contacts/index.html', context)

def addContact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/contacts')

def deleteContact(request, id):
    contacts = Contact.objects.get(pk = id)
    contacts.delete()
    return redirect('/contacts')

def updateContact(request, id):
    contact = Contact.objects.get(pk = id)
    updateForm = ContactForm(instance = contact)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance = contact)
        if form.is_valid():
            form.save()
            return redirect('/contacts')
    context = {
        'updateForm' : updateForm,
        'key' : id,
        'contacts' : Contact.objects.all(),
    }
    return render(request, 'contacts/index.html', context)

def filterContact(request, id):
    contacts = Contact.objects.filter(contact_company = id)
    form = ContactForm(request.POST)
    context = {
        'contacts' : contacts,
        'form' : form
    }
    return render(request, 'contacts/index.html', context)