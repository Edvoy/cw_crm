from django import forms
from django.forms import ModelForm

from .models import Email

class EmailForm(ModelForm):

    from_email = Email
    to_email = forms.CharField(required = False,
                        max_length = 100,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'email', 
                             }
                         ),
                     )
    email_subject = forms.CharField(
                        widget = forms.TextInput(
                            attrs = {
                                'class' : 'form-control',
                                'placeholder' : 'firstname', 
                            }
                        )
                    )
    email_message = forms.CharField(
                        widget = forms.TextInput(
                            attrs = {
                                'class' : 'form-control',
                                'placeholder' : 'firstname', 
                            }
                        )
                    )

    class Meta:
        model = Email
        fields = '__all__'