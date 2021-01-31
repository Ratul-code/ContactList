from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=31)
    email=models.CharField(max_length=80)
    relation=models.CharField(max_length=30)
    address=models.CharField(max_length=200)
    created_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    