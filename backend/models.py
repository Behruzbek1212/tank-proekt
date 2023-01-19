from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=255)

    def  __str__(self):
        return self.name
    
class  Branding(models.Model):
    name = models.CharField(max_length=255)
    price = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)