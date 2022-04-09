from django.db import models

# Create your models here.


class Contact(models.Model):
    Username = models.CharField(max_length=255)
    UserEmail = models.CharField(max_length=50)
    Subject = models.CharField(max_length=255)
    Message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message From " + self.Username 