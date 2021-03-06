from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('contacts', views.listContact, name="List_Contacts"),
    path('addContact', views.addContact, name="Add_Contact"),
    path('deleteContact/<int:id>', views.deleteContact, name="Delete_Contact"),
    path('updateContact/<int:id>', views.updateContact, name="Update_Contact"),
    path('filterContact/<int:id>', views.filterContact, name="Filter_Contact"),
]

