from django.db  import models
from useraccount.models.users import User
class Borrowers(models.Model):
    # user_id=models.CharField(max_length=3,primary_key=True,blank=False,null=False)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    GENDER_CHOICES=(
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    WORKING_STATUS=(
        ('Owner', 'Owner'),
        ('Employee', 'Employee'),
        ('Student', 'Student'),
        ('Overseas Worker', 'Overseas Worker'),
        ('Pensioner', 'Pensioner'),
        ('Unemployed', 'Unemployed'),
    )
    gender=models.CharField(max_length=15,choices=GENDER_CHOICES)
    country=models.CharField(max_length=50,default='IN')
    title=models.CharField(max_length=15)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    unique_number=models.CharField(max_length=30)
    dob=models.DateField()
    address=models.TextField()
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=50)
    bussiness_name=models.CharField(max_length=100)
    working_status=models.CharField(max_length=100,choices=WORKING_STATUS)
    photo=models.ImageField(upload_to='images/')
    note=models.TextField()
    files=models.FileField(upload_to='files/')
    loan_officers_access=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(auto_now=True)
    is_decline=models.BooleanField(default=False)
    is_approve=models.BooleanField(default=False)
    is_blacklist=models.BooleanField(default=False)

    # username=models.CharField(max_length=50)
    # password=models.CharField(max_length=20)
    # month=models.DateField()
    # year=models.DateField()
    # SOURCE_CHOICES = (
    #     ('Online', 'Online'),
    #     ('Admin', 'Admin'),
    # )
    # source=models.CharField(ma    x_length=30,choices=SOURCE_CHOICES)
    # ACTIVE_CHOICES=(
    #     ('Yes','Yes'),
    #     ('No','No'),
    # )
    # active=models.CharField(max_length=30,choices=ACTIVE_CHOICES)
    # def _str_(self):
    #     return self.user_id
    def __str__(self):
        return self.first_name +' '+ self.last_name

