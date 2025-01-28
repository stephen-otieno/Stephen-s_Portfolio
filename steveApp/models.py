from django.db import models

class Contacts(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.CharField(max_length=100)
    client_message = models.TextField()

    def __str__(self):
        return self.client_name


# Create your models here.kl