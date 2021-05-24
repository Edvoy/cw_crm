from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from emails.views import syncMailsWhenUpdateContact


def listContact(request):
    """
    Display all contacts in contact tab
    """
    contacts = Contact.objects.all()
    form = ContactForm()
    context = {
        'contacts' : contacts,
        'form' : form
    }
    return render(request, 'contacts/index.html', context)

def addContact(request):
    """
    Add new contact with contact form in contact tab
    """
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/contacts')

def deleteContact(request, id):
    """
    Delete contact with delete button on contact card in contact tab
    """
    contacts = Contact.objects.get(pk = id)
    contacts.delete()
    return redirect('/contacts')

def updateContact(request, id):
    """
    Update contact with update button on contact card in contact tab
    """
    contact = Contact.objects.get(pk = id)
    updateForm = ContactForm(instance = contact)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance = contact)
        if form.is_valid():
            form.save()
            syncMailsWhenUpdateContact()
            return redirect('/contacts')
    context = {
        'updateForm' : updateForm,
        'key' : id,
        'contacts' : Contact.objects.all(),
    }
    return render(request, 'contacts/index.html', context)

def filterContact(request, id):
    """
    Contact filter when user click on filter button in company tab
    Contact are filter by company and display all contact in this company
    """
    contacts = Contact.objects.filter(contact_company = id)
    form = ContactForm(request.POST)
    context = {
        'contacts' : contacts,
        'form' : form
    }
    return render(request, 'contacts/index.html', context)