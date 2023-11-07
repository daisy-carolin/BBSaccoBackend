from django.db import models

class AddBorrowersGroup(models.Model):
    name=models.CharField(max_length=250,unique=True,blank=False,null=False,)
    notes=models.TextField(blank=False,null=False)