from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm

def index(request):
    companies = Company.objects.all()
    form = CompanyForm()
    context = {
        'companies' : companies,
        'form' : form
    }
    return render(request, 'main_crm/index.html', context)

def addCompany(request):
    form = CompanyForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')

def deleteCompany(request, id):
    company = Company.objects.get(pk = id)
    company.delete()
    return redirect('/')

def updateCompany(request, id):
    company = Company.objects.get(pk = id)
    updateForm = CompanyForm(instance = company)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance = company)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'updateForm' : updateForm,
        'key' : id,
        'companies' : Company.objects.all(),
    }
    return render(request, 'main_crm/index.html', context)