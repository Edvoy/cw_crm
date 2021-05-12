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
    return render(request, 'index.html', context)

def addContact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/listContact')

def deleteContact(request, id):
    contacts = Contact.objects.get(pk = id)
    contacts.delete()
    return redirect('/listContact')

def updateContact(request, id):
    contacts = Contact.objects.get(pk = id)
    updateForm = ContactForm(instance = contacts)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance = contacts)
        if form.is_valid():
            form.save()
            return redirect('/listContact')
    context = {
        'updateForm' : updateForm,
        'key' : id,
        'contacts' : Contact.objects.all(),
    }
    return render(request, 'index.html', context)