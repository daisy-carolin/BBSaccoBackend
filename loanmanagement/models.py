from django.db import models

# Create your models here.

class Borrowers(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,blank=False,null=False)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    GENDER_CHOICES=(
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender=models.CharField(max_length=15,choices=GENDER_CHOICES)
    country=models.CharField(max_length=30)
    title=models.CharField(max_length=15)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    unique_number=models.CharField(max_length=30)
    dob=models.DateField()
    address=models.TextField()
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    bussiness_name=models.CharField(max_length=100)
    working_status=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images/')
    note=models.TextField()
    files=models.FileField(upload_to='files/')
    loan_officers=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(auto_now=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    month=models.DateField()
    year=models.DateField()
    SOURCE_CHOICES = (
        ('Online', 'Online'),
        ('Admin', 'Admin'),
    )
    source=models.CharField(max_length=30,choices=SOURCE_CHOICES)
    ACTIVE_CHOICES=(
        ('Yes','Yes'),
        ('No','No'),
    )
    active=models.CharField(max_length=30,choices=ACTIVE_CHOICES)
    def _str_(self):
        return self.user_id

class CostomField(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    category=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    field_type=models.CharField(max_length=50)
    required=models.CharField(max_length=50)

class Loans(models.Model):
    user_id = models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    borrowers_id=models.ForeignKey(Borrowers,on_delete=models.CASCADE)
    loan_product_id=models.CharField(max_length=15)
    reference=models.CharField(max_length=30)
    release_date=models.DateField()
    maturity_date=models.DateField()
    month=models.CharField(max_length=15)
    year=models.CharField(max_length=15)
    interest_start_date=models.DateField()
    first_payment_date=models.DateField()
    loan_disbursed_by_id=models.CharField(max_length=3)
    principal=models.FloatField()
    interest_method=models.FloatField()
    interest_rate=models.FloatField()
    interest_period=models.DateField()
    override_interest=models.FloatField()
    override_interest_amount=models.FloatField()
    loan_duration=models.CharField(max_length=15)
    loan_duration_type=models.DateField()
    repayment_cycle=models.DateField()
    decimal_places=models.CharField(max_length=30)
    repayment_order=models.CharField(max_length=30)
    loan_fees_sheduale=models.CharField(max_length=30)
    grace_on_interest_charged=models.FloatField()
    loan_status_id=models.CharField(max_length=30)
    files=models.FileField(upload_to='files/')
    description=models.TextField()
    loan_status=models.CharField(max_length=15)
    balance=models.FloatField()
    override=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=15)
    applied_amount=models.FloatField()
    approved_amount=models.FloatField()
    disbursed_notes=models.CharField(max_length=50)
    withdrawn_notes=models.CharField(max_length=50)
    closed_notes=models.CharField(max_length=50)
    rescheduled_notes=models.CharField(max_length=50)
    declined_notes=models.CharField(max_length=50)
    written_off_notes=models.CharField(max_length=50)
    approved_date=models.DateField()
    disbursed_date=models.DateField()
    withdrawn_date=models.DateField()
    closed_date=models.DateField()
    rescheduled_date=models.DateField()
    declined_date=models.DateField()
    written_off_date=models.DateField()
    approved_by_id=models.CharField(max_length=3)
    disbursed_by_id=models.CharField(max_length=3)
    withdrawn_by_id=models.CharField(max_length=3)
    declined_by_id=models.CharField(max_length=3)
    written_off_by_id=models.CharField(max_length=3)
    rescheduled_by_id=models.CharField(max_length=3)
    closed_by_id=models.CharField(max_length=3)
    def _str_(self):
        return self.user_id

class LoanApplication(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    borrower_id=models.ForeignKey(Borrowers,on_delete=models.CASCADE)
    loan_product_id=models.CharField(max_length=3)
    amount=models.FloatField()
    STATUS_CHOICES = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Declined', 'Declined'),
    )
    status=models.CharField(max_length=15,choices=STATUS_CHOICES)
    notes=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

class LoanComment(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    loan_id=models.ForeignKey(Loans,on_delete=models.CASCADE)
    notes=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class LoanDisbursedBy(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    name=models.CharField(max_length=30)

class LoanFees(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    name=models.CharField(max_length=30)
    FEES_TYPE_CHOICES=(
        ('Fixed','Fixed'),
        ('Percentage','Percentage'),
    )
    loan_fees_type=models.CharField(max_length=15,choices=FEES_TYPE_CHOICES)
    def _str_(self):
        return self.user_id

class LoanFeesMeta(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    category=models.CharField(max_length=30)
    parent_id=models.CharField(max_length=30)
    loan_fees_id=models.ForeignKey(LoanFees,on_delete=models.CASCADE)
    value=models.CharField(max_length=30)
    loan_fees_schedule=models.CharField(max_length=30)
class LoanProduct(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    name=models.CharField(max_length=30)
    loan_disbursed_by_id=models.CharField(max_length=15)
    minimum_principal=models.FloatField()
    defoult_principal=models.FloatField()
    maximum_principal=models.FloatField()
    INTEREST_METHOD_CHOICES=(
        ('Flate rate','Flate rate'),
        ('Declining balance equal install','Declining balance equal install'),
    )
    interest_method=models.CharField(max_length=35,choices=INTEREST_METHOD_CHOICES)
    interest_rate=models.FloatField()
    INTEREST_PERIOD_CHOICES=(
        ('D','Day'),
        ('W','Week'),
        ('M','Month'),
        ('Y','Year'),
    )
    interest_period=models.CharField(max_length=30,choices=INTEREST_PERIOD_CHOICES)
    minimum_interest_rate=models.FloatField()
    defoult_interest_rate=models.FloatField()
    maximum_interest_rate=models.FloatField()
    override_interest=models.CharField(max_length=30)
    override_interest_amount=models.FloatField()
    defoult_loan_duration=models.CharField(max_length=15)
    DURATION_TYPE_CHOICES=(
        ('D','Day'),
        ('W','Week'),
        ('M','Month'),
        ('Y','Year'),
    )
    defoult_loan_duration_type=models.CharField(max_length=30,choices=DURATION_TYPE_CHOICES)
    REPAYMENT_CYCLE_CHOICES=(
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
    )
    repayment_cycle=models.CharField(max_length=30,choices=REPAYMENT_CYCLE_CHOICES)
    decimal_places=models.CharField(max_length=15)
    repayment_order=models.CharField(max_length=30)
    loan_fees_schedule=models.CharField(max_length=30)
    branch_access=models.CharField(max_length=50)
    grace_on_interest_charged=models.CharField(max_length=50)
    advanced_enabled=models.CharField(max_length=30)
    enable_late_repayment_penality=models.CharField(max_length=30)
    enable_after_maturity_date_penality=models.CharField(max_length=30)
    PENALITY_TYPE_CHOICES=(
        ('Percentage','Percentage'),
        ('fixed','Fixed'),
    )
    after_maturity_date_penality=models.CharField(max_length=30,choices=PENALITY_TYPE_CHOICES)
    REPAY_PENALITY_TYPE_CHOICES=(
        ('Percentage','Percentage'),
        ('fixed','Fixed'),
    )
    late_repayment_penalty_type=models.CharField(max_length=30,choices=REPAY_PENALITY_TYPE_CHOICES)
    REPAY_PENALITY_CALCULATE_CHOICES=(
        ('Overdue Principal','Overdue Principal'),
        ('Overdue Principal inter','Overdue Principal inter'),
    )
    late_repayment_penalty_calculate=models.CharField(max_length=35,choices=REPAY_PENALITY_CALCULATE_CHOICES)
    AFTER_MATURITY_DATE_PENALTY_CALCULATE_CHOICES=(
        ('Overdue Principal', 'Overdue Principal'),
        ('Overdue Principal inter', 'Overdue Principal inter')
    )
    after_maturity_date_penality_calculate=models.CharField(max_length=30,choices=AFTER_MATURITY_DATE_PENALTY_CALCULATE_CHOICES)
    late_repayment_penalty_amount=models.FloatField()
    after_maturity_date_penality_amount=models.FloatField()
    late_repayment_penalty_grace_period=models.CharField(max_length=30)
    after_maturity_date_penality_grace_period=models.CharField(max_length=30)
    late_repayment_penalty_recurring=models.CharField(max_length=30)
    after_maturity_date_penality_recurring=models.CharField(max_length=30)

class LoanRepayments(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    loan_id=models.ForeignKey(Loans,on_delete=models.CASCADE)
    borrower_id=models.ForeignKey(Borrowers,on_delete=models.CASCADE)
    amount=models.FloatField()
    repayment_method_id=models.CharField(max_length=30)
    collection_date=models.DateField()
    notes=models.CharField(max_length=100)
    month=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    due_date=models.DateField()
    craeted_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(auto_now=True)

class LoanRepaymentMethods(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    name=models.CharField(max_length=50)

class LoanSchedules(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    loan_id=models.ForeignKey(Loans,on_delete=models.CASCADE)
    borrower_id=models.ForeignKey(Borrowers,on_delete=models.CASCADE)
    description=models.CharField(max_length=100)
    due_date=models.DateField()
    month=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    principal=models.FloatField()
    principal_balance=models.FloatField()
    interest=models.FloatField()
    fees=models.FloatField()
    penalty=models.FloatField()
    due=models.FloatField()
    sytem_generated=models.CharField(max_length=30,default=0)
    close=models.CharField(max_length=30,default=0)
    missed=models.CharField(max_length=30,default=0)
    missed_penalty_applied=models.CharField(max_length=30,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(auto_now=True)

class LoanStatus(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    name=models.CharField(max_length=30)
    text_color=models.CharField(max_length=30)
    background_color=models.CharField(max_length=30)

class Savings(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    borrower_id=models.ForeignKey(Borrowers,on_delete=models.CASCADE)
    savings_product_id=models.CharField(max_length=3)
    note=models.CharField(max_length=100)
    data=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def _str_(self):
        return self.user_id

class SavingFees(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    name=models.CharField(max_length=30)
    saving_products=models.CharField(max_length=100)
    amount=models.FloatField()
    fees_posting=models.CharField(max_length=30)
    fees_adding=models.CharField(max_length=30)
    FEES_TYPE_CHOICES=(
        ('Full','Full'),
        ('Pro_rate','Pro_rate'),
    )
    new_fees_type=models.CharField(max_length=30,choices=FEES_TYPE_CHOICES)
    notes=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class SavingsProducts(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    name=models.CharField(max_length=30)
    allow_overdraw=models.CharField(max_length=30)
    interest_rate=models.FloatField()
    minimum_balance=models.FloatField()
    interest_posting=models.CharField(max_length=30)
    interest_adding=models.CharField(max_length=30)
    notes=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class SavingsTransactions(models.Model):
    user_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    borrower_id=models.ForeignKey(Borrowers,on_delete=models.CASCADE)
    savinga_id=models.ForeignKey(Savings,on_delete=models.CASCADE)
    amount=models.FloatField()
    TYPE_CHOICES=(
        ('Deposit','Deposit'),
        ('Withdrawal','Withdrawal'),
        ('Bank Fees','Bank Fees'),
    )
    type=models.CharField(max_length=30,choices=TYPE_CHOICES)
    system_interest=models.CharField(max_length=30)
    date=models.DateField()
    time=models.CharField(max_length=10)
    year=models.CharField(max_length=10)
    month=models.CharField(max_length=10)
    notes=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
class LoanRegister(models.Model):
    lr_id=models.CharField(max_length=3,primary_key=True)
    lr_type=models.CharField(max_length=30)
    lr_member_name=models.CharField(max_length=50)
    lr_member_no=models.IntegerField()
    lr_member_phone_no=models.BigIntegerField()
    lr_member_email=models.EmailField()
    lr_loan_amt=models.FloatField()
    lr_loan_s_date=models.DateField()
    lr_loan_e_date=models.DateField()
    lr_disbursement_account=models.CharField(max_length=50)
    lr_disbursement_date=models.DateField()
    lr_enter_repayment_period_months=models.CharField(max_length=30)
    lr_guarantor_name1=models.CharField(max_length=50)
    lr_guaranteed_amt1=models.FloatField()
    lr_comment_1=models.CharField(max_length=100)
    lr_guarantor_name2=models.CharField(max_length=50)
    lr_guaranteed_amt2=models.FloatField()
    lr_comment_2=models.CharField(max_length=100)
    lr_guarantor_name3=models.CharField(max_length=50)
    lr_guaranteed_amt3=models.FloatField()
    lr_comment_3=models.CharField(max_length=100)
    lr_interest_rate=models.CharField(max_length=30)
    lr_duration=models.CharField(max_length=15)
    lr_status=models.CharField(max_length=20)
    lr_processing_fee=models.CharField(max_length=30)
    lr_late_pay_fine=models.CharField(max_length=30)
    lr_ost_balance_fine_date=models.DateField()
    lr_ost_loan_blance_fine=models.CharField(max_length=30)
    lr_fine_diferment=models.CharField(max_length=30)
    def __str__(self):
        return self.lr_id

class LoanInsRegister(models.Model):
    lir_id=models.CharField(max_length=3,primary_key=True,)
    lir_reference=models.ForeignKey(LoanRegister,on_delete=models.CASCADE)
    lir_desc=models.CharField(max_length=100)
    lir_invoice_date=models.DateField()
    lir_due_date=models.DateField()
    lir_payable=models.CharField(max_length=30)
    lir_interest=models.CharField(max_length=30)
    lir_principal=models.CharField(max_length=30)
    lir_paiid=models.CharField(max_length=30)
    lir_balance=models.CharField(max_length=30)
    lir_status=models.CharField(max_length=50)
    lir_principal_penalty=models.CharField(max_length=30)
    lir_interest_penalty=models.CharField(max_length=30)
    lir_penalty_interest=models.CharField(max_length=30)

