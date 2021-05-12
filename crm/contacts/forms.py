from django import forms
from django.forms import ModelForm

from .models import Contact

class ContactForm(ModelForm):

    COMPANY_CHOICES = (
        ('LOW', "Low"),
        ('MEDIUM', "Medium"),
        ('HIGH', "High"),
        ('NONE', "priorité"),
    )

    contact_first_name = forms.CharField(max_length=255,
                        widget = forms.TextInput(
                            attrs = {
                                'class' : 'form-control',
                                'placeholder' : 'company name', 
                            }
                        )
                    )
    contact_last_name = forms.CharField(max_length=255,
                        widget = forms.TextInput(
                            attrs = {
                                'class' : 'form-control',
                                'placeholder' : 'company name', 
                            }
                        )
                    )
    contact_company = forms.CharField(required = False,
                        max_length = 255,
                         widget = forms.Select(
                            choices = COMPANY_CHOICES, 
                            attrs = {
                                'class' : 'form-control',
                                'placeholder' : 'priorité', 
                            }
                         ),
                     )
    contact_job = forms.CharField(required = False,
                        max_length = 50,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'zip code', 
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