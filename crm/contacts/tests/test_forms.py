from django.test import TestCase
from django.utils import timezone
from datetime import date

from contacts.models import Contact
from companies.models import Company
from contacts.forms import ContactForm

class Setup_Class(TestCase):
       
        def setUp(self):
            Contact.objects.create(
                contact_first_name = "Jean",
                contact_last_name = "Durnant",
                contact_company = "Super Company",
                contact_job = "CTO", 
                contact_email = "jean@company.com",
                contact_phone = "+33687120463",
                contact_notes = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id porta felis. Vivamus felis urna, feugiat a erat nec, molestie viverra urna. Nam consequat nisl sem, et fringilla urna sagittis a."
                )
            Company.objects.create(
                company_name = "Super Company",
                company_adress = "6 rue du paradis",
                company_zip_code = "75001",
                company_city = "Paris", 
                company_email = "super@company.com",
                company_phone = "+33687129463",
                company_notes = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id porta felis. Vivamus felis urna, feugiat a erat nec, molestie viverra urna. Nam consequat nisl sem, et fringilla urna sagittis a."
                )

class AddContactFormTest(TestCase):
    
    def test_valid_form(self):
        data = {
            "contact_first_name": "Jean",
            "contact_last_name": "Durnant",
            "contact_company": "Super Company",
            "contact_job": "CTO", 
            "contact_email": "jean@company.com",
            "contact_phone": "+33687120463",
            "contact_notes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id porta felis. Vivamus felis urna, feugiat a erat nec, molestie viverra urna. Nam consequat nisl sem, et fringilla urna sagittis a."
            }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_unvalid_form(self):
        data = {
             "contact_first_name": "",
            "contact_last_name": "",
            "contact_company": "",
            "contact_job": "CTO", 
            "contact_email": "jean@company.com",
            "contact_phone": "+33687120463",
            "contact_notes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id porta felis. Vivamus felis urna, feugiat a erat nec, molestie viverra urna. Nam consequat nisl sem, et fringilla urna sagittis a."
            }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())