from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ticket(models.Model):
    subject = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    priority = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    category = models.CharField(max_length=100)