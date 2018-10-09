from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Volunteer(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

class Blog(models.Model):
    blog_no = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=1000)
    text = models.CharField(max_length=100000)
