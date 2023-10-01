from django.db import models

# Create your models here.


class CustomerRequest(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    type_of_service = models.CharField(max_length=50)
    device_name = models.CharField(max_length=100)
    request_date = models.DateTimeField()
    is_done = models.BooleanField()

    def __str__(self):
        return self.name
