from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=50)	
	content = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)