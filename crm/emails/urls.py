from django.urls import path
from . import views

app_name = 'emails'
urlpatterns = [
    path('emails', views.listEmail, name="List_Emails"),
    path('filterContactEmails/<int:id>', views.filterEmailFromContact, name="Filter_Email_From_Contact"),
    path('filterCompanyEmails/<int:id>', views.filterEmailFromCompany, name="Filter_Email_From_Company"),
    path('deleteEmails/<int:id>', views.deleteEmail, name="Delete_Email"),
]