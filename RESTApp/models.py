from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
