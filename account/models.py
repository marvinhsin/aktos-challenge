from django.db import models

# Create your models here.
class Account(models.Model):
    client_id = models.CharField(max_length = 100, unique = True)
    balance = models.DecimalField(max_digits = 10, decimal_places = 2)
    status = models.CharField(max_length = 100)
    consumer_name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    ssn = models.CharField(max_length = 11)

    def __str__(self):
        return f'{self.consumer_name} - Client ID: {self.client_id}'