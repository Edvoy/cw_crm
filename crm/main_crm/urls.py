from django.urls import path, include
from . import views

app_name = 'main_crm'
urlpatterns = [
    path('', views.index, name="home"),
    path('addCompany', views.addCompany, name="Add Company"),
    path('deleteCompany/<int:id>', views.deleteCompany, name="Delete Company"),
    path('updateCompany/<int:id>', views.updateCompany, name="Update Company"),
]