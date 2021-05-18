from django.db import models
from contacts.models import Contact

class Email(models.Model):
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE,blank=True)
    from_email = models.EmailField(max_length=200)
    to_email =models.EmailField(max_length=200)
    email_subject = models.CharField(max_length=200)
    email_message = models.CharField(max_length=200)
    receive_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["receive_time"]

    def __str__(self):
        return self.from_email