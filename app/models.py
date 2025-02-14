from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    text = models.CharField(max_length=400, null=False, blank=False)
