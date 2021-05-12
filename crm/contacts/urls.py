from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('listContact', views.listContact, name="List_Contacts"),
    path('addCompany', views.addCompany, name="Add_Contact"),
    path('deleteCompany/<int:id>', views.deleteCompany, name="Delete_Contact"),
    path('updateCompany/<int:id>', views.updateCompany, name="Update_Contact"),
]