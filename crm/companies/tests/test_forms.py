from django.test import TestCase
from django.utils import timezone
from datetime import date

from companies.models import Company
from companies.forms import CompanyForm

class Setup_Class(TestCase):
       
        def setUp(self):
            Company.objects.create(
                company_name = "Super Company",
                company_adress = "6 rue du paradis",
                company_zip_code = "75001",
                company_city = "Paris", 
                company_email = "super@company.com",
                company_phone = "+33687129463",
                company_notes = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id porta felis. Vivamus felis urna, feugiat a erat nec, molestie viverra urna. Nam consequat nisl sem, et fringilla urna sagittis a."
                )

class AddCompanyFormTest(TestCase):
    
    def test_valid_form(self):
        data = {
            "company_name": "Super Company",
            "company_adress": "6 rue du paradis",
            "company_zip_code": "75001",
            "company_city": "Paris", 
            "company_email": "super@company.com",
            "company_phone": "+33687129463",
            "company_notes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id porta felis. Vivamus felis urna, feugiat a erat nec, molestie viverra urna. Nam consequat nisl sem, et fringilla urna sagittis a."
            }
        form = CompanyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_unvalid_form(self):
        data = {
            "company_name": "",
            "company_adress": "",
            "company_zip_code": "",
            "company_city": "", 
            "company_email": "",
            "company_phone": "",
            "company_notes": ""
            }
        form = CompanyForm(data=data)
        self.assertFalse(form.is_valid())