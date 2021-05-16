from django.db import models

class Email(models.Model):
    from_email = models.EmailField(max_length=200)
    to_email = models.ForeignKey('contacts.Contact', on_delete=models.CASCADE,)
    email_subject = models.CharField(max_length=200)
    email_message = models.CharField(max_length=200)
    receive_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["receive_time"]

    def __str__(self):
        return self.from_email