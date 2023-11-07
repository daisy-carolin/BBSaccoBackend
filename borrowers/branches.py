from django.db import models
from useraccount.models.users import User
class Branch(models.Model):
    name = models.CharField(max_length=50,unique=True,null=False,blank=False)
    notes = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
class AddUserInBranch(models.Model):
    branch_id=models.ForeignKey(Branch,on_delete=models.CASCADE,editable=False)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    added_at=models.DateTimeField(auto_now_add=True)

