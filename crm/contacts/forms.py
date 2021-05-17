from django import forms
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Contact
from django.core.validators import RegexValidator

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
    
    contact_job = forms.CharField(required = True,
                        max_length = 50,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'job', 
                             }
                         ),
                     )
    contact_email = forms.EmailField(required=True,widget = forms.EmailInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'email', 
                             }))
    
    
    # todo: comprendre pourquoi la gestion d'erreurs de contact_phonene fonctionne pas
    # contact_phone = forms.RegexField(regex='^\+?1?\d{9,15}$',error_messages = {"Invalid": "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."})
    
    # contact_phone = PhoneNumberField()

    # contact_phone = forms.CharField(required = True,
    #                 max_length = 100,
    #                 validators=[
    #                         RegexValidator(
    #                         regex='^\+?1?\d{9,15}$',
    #                         message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    #                         code='invalid_username'
    #                         )
    #                 ],
    #                 widget = forms.TextInput(
    #                          attrs = {
    #                              'class' : 'form-control',
    #                              'placeholder' : 'phone number', 
    #                         }
    #                 )
    # )

    contact_phone = forms.CharField(required = True,
                        max_length = 100,
                        widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'phone number (+33333333333)', 
                             }
                         )
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