from django.db import models

# Create your models here.

class Cnab(models.Model):
    transaction_type = models.CharField(max_length=1)    
    transaction_date = models.DateField() 
    transaction_value = models.FloatField()
    transaction_cpf = models.CharField(max_length=11) 
    transaction_card = models.CharField(max_length=12)
    transaction_hour = models.CharField(max_length=6) 
    transaction_shop_owner = models.CharField(max_length=14)
    transaction_shop_name = models.CharField(max_length=19)
