from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm
from emails.views import syncMailsWhenUpdateCompany

def listCompanies(request):
    """
    Display all companies in company tab
    """
    companies = Company.objects.all()
    form = CompanyForm()
    context = {
        'companies' : companies,
        'form' : form
    }
    return render(request, 'companies/index.html', context)

def addCompany(request):
    """
    Add new company with company form in company tab
    """
    form = CompanyForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/companies')

def deleteCompany(request, id):
    """
    Delete company with delete button on company card in company tab
    """
    company = Company.objects.get(pk = id)
    company.delete()
    return redirect('companies/index.html')

def updateCompany(request, id):
    """
    Update company with update button on company card in company tab
    """
    company = Company.objects.get(pk = id)
    updateForm = CompanyForm(instance = company)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance = company)
        if form.is_valid():
            form.save()
            syncMailsWhenUpdateCompany()
            return redirect('/companies')
    context = {
        'updateForm' : updateForm,
        'key' : id,
        'companies' : Company.objects.all(),
    }
    return render(request, 'companies/index.html', context)

