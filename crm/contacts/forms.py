from django import forms
from django.forms import ModelForm

from .models import Contact

class ContactForm(ModelForm):

    contact_first_name = forms.CharField(max_length=255,
                        widget = forms.TextInput(
                            attrs = {
                                'class' : 'form-control',
                                'placeholder' : 'firstname', 
                            }
                        )
                    )
    contact_last_name = forms.CharField(max_length=255,
                        widget = forms.TextInput(
                            attrs = {
                                'class' : 'form-control',
                                'placeholder' : 'lastname', 
                            }
                        )
                    )
    contact_company = Contact 
    
    contact_job = forms.CharField(required = False,
                        max_length = 50,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'job', 
                             }
                         ),
                     )
    contact_email = forms.CharField(required = False,
                        max_length = 100,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'email', 
                             }
                         ),
                     )
    contact_phone = forms.CharField(required = False,
                        max_length = 100,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'phone number', 
                             }
                         ),
                     )
    contact_notes = forms.CharField(required = False,
                        max_length = 550,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'notes', 
                             }
                         ),
                     )

    class Meta:
        model = Contact
        fields = '__all__'