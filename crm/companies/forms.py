from django import forms
from django.forms import ModelForm

from .models import Company

class CompanyForm(ModelForm):
    company_name = forms.CharField(max_length=255,
                        widget = forms.TextInput(
                            attrs = {
                                'class' : 'form-control',
                                'placeholder' : 'company name', 
                            }
                        )
                    )
    company_adress = forms.CharField(required = False,
                        max_length = 255,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'adress', 
                             }
                         ),
                     )
    company_zip_code = forms.CharField(required = False,
                        max_length = 50,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'zip code', 
                             }
                         ),
                     )
    company_city = forms.CharField(required = False,
                        max_length = 100,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'city', 
                             }
                         ),
                     )
    company_email = forms.CharField(required = False,
                        max_length = 100,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'email', 
                             }
                         ),
                     )
    company_phone = forms.CharField(required = False,
                        max_length = 100,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'phone number', 
                             }
                         ),
                     )
    company_notes = forms.CharField(required = False,
                        max_length = 550,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'notes', 
                             }
                         ),
                     )

    class Meta:
        model = Company
        fields = '__all__'