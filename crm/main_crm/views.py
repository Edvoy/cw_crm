from django.shortcuts import render, redirect
from .models import Company
from .forms import AddCompanyForm

def index(request):
    companies = Company.objects.all()
    formatted_companies = ["<li>{}</li>".format(companies.company_name) for company in companies]
    context = {
        'company' : companies,
    }
    return render(request, 'companies/index.html', context)

def addCompany(request):
    form = AddCompanyForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')

def deleteCompany(request, id):
    company = Company.objects.get(pk = id)
    company.delete()
    return redirect('/')

def updateCompany(request, id):
    company = Company.objects.get(pk = id)
    updateForm = AddCompanyForm(instance = company)
    if request.method == 'POST':
        form = AddCompanyForm(request.POST, instance = company)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'updateForm' : updateForm,
        'key' : id,
        'company' : Company.objects.all(),
    }
    return render(request, 'companies/index.html', context)