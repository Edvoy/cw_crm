from django.urls import path
from . import views

app_name = 'emails'
urlpatterns = [
    path('emails', views.listEmail, name="List_Emails"),
]