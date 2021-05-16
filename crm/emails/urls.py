from django.urls import path
from . import views

app_name = 'emails'
urlpatterns = [
    path('emails', views.listEmail, name="List_Emails"),
    path('filterEmails/<int:id>', views.filterEmail, name="Filter_Email"),
    path('deleteEmails/<int:id>', views.deleteEmail, name="Delete_Email"),
]