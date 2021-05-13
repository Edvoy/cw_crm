from django.urls import path
from . import views

app_name = 'companies'
urlpatterns = [
    path('', views.listCompanies, name="List_Companies"),
    path('companies', views.listCompanies, name="List_Companies"),
    path('addCompany', views.addCompany, name="Add_Company"),
    path('deleteCompany/<int:id>', views.deleteCompany, name="Delete_Company"),
    path('updateCompany/<int:id>', views.updateCompany, name="Update_Company"),
]
