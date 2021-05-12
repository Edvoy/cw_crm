from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def listContact(request):
    contacts = Contact.objects.all()
    form = ContactForm()
    context = {
        'companies' : contacts,
        'form' : form
    }
    return render(request, 'contacts/index.html', context)

def addCompany(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')

def deleteCompany(request, id):
    contacts = Contact.objects.get(pk = id)
    contacts.delete()
    return redirect('/')

def updateCompany(request, id):
    contacts = Contact.objects.get(pk = id)
    updateForm = ContactForm(instance = contacts)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance = contacts)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'updateForm' : updateForm,
        'key' : id,
        'companies' : Contact.objects.all(),
    }
    return render(request, 'contacts/index.html', context)