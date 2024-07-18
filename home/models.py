from django.db import models

# Create your models here.

class fixtures(models.Model):
    home = models.CharField(max_length=100, blank=False, null=False)
    away = models.CharField(max_length=100, blank=False, null=False)
    date = models.CharField(max_length=100, blank=False, null=False)
    stadium = models.CharField(max_length=100, blank=False, null=False)
    town = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        
        return self.home
    
class results(models.Model):
    home = models.CharField(max_length=100, blank=False, null=False)
    away = models.CharField(max_length=100, blank=False, null=False)
    date = models.CharField(max_length=100, blank=False, null=False)
    stadium = models.CharField(max_length=100, blank=False, null=False)
    town = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        
        return self.home