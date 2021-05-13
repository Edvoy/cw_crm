from django.shortcuts import render

def listEmails(request):
    contacts = Contact.objects.all()
    form = ContactForm()
    context = {
        'contacts' : contacts,
        'form' : form
    }
    return render(request, 'contacts/index.html', context)