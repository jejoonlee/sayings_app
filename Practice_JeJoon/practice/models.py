from django.db import models

# Create your models here.
class Practice(models.Model):
  title = models.CharField(max_length=80)
  content = models.TextField(default=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)