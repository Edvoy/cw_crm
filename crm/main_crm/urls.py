from django.urls import path, include
from . import views

app_name = 'main_crm'
urlpatterns = [
    path('', views.index, name="Home"),
    path('addCompany', views.addCompany, name="Add_Company"),
    path('deleteCompany/<int:id>', views.deleteCompany, name="Delete_Company"),
    path('updateCompany/<int:id>', views.updateCompany, name="Update_Company"),
]