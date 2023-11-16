from django.db import models

# Create your models here.

class Cont_categories(models.Model):
    CAT_TYPE_CHOICES=(
        ('Share Capital','Share Capital'),
        ('Savings Contribution','Savings Contribution'),
        ('Welfare/Committee Contribution','Welfare/Committee Contribution'),
        ('Membership/Entry Fee Contribution','Membership/Entry Fee Contribution'),
        ('Investment Contribution','Investment Contribution'),
        ('Other Contribution','Other Contribution')
    )
    cate_id=models.CharField(max_length=3,null=False,blank=False,primary_key=True)
    cate_type=models.CharField(max_length=100,null=False,blank=False,choices=CAT_TYPE_CHOICES)
    cate_desciption=models.CharField(max_length=200,null=True,blank=True)
    cate_balance=models.FloatField()
    def _str_(self):
        return self.cate_type

class Contributions(models.Model):
    con_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    con_name=models.CharField(max_length=100,null=True,blank=True)
    amt_pr_member=models.CharField(max_length=200,null=False,blank=False)
    con_cat=models.ForeignKey(Cont_categories,on_delete=models.CASCADE)
    CON_TYPE_CHOICES=(
        ('Regular Contribution','Regular Contribution'),
        ('One Time Contribution','One Time Contribution'),
        ('No Scheduled Contribution','No Scheduled Contribution')
    )
    con_type=models.CharField(max_length=100,choices=CON_TYPE_CHOICES)
    DISABLE_CHOICES=(
        ('Yes','Yes'),
        ('No','No')
    )
    con_disable=models.CharField(max_length=3,choices=DISABLE_CHOICES)
    SEND_CHOICES=(
        ('Yes','Yes'),
        ('No','No')
    )
    send_invoice_reminder=models.CharField(max_length=3,choices=SEND_CHOICES)
    ENABLE_CHOICES=(
        ('Yes','Yes'),
        ('No','No')
    )
    con_enable=models.CharField(max_length=3,choices=ENABLE_CHOICES)
    DISPLAY_CHOICES=(
        ('Yes','Yes'),
        ('No','No')
    )
    con_display_memeber=models.CharField(max_length=3,choices=DISPLAY_CHOICES)
    def _str_(self):
        return self.con_id

class GroupAaccounts(models.Model):
    ga_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    GA_TYPE_CHOICES=(
        ('Bank Account','Bank Account'),
        ('Sacco Account','SACCO Account'),
        ('Mobile Account','Mobile Account'),
        ('Petty Cash Account','Petty Cash Account'),
    )
    ga_type=models.CharField(max_length=100,choices=GA_TYPE_CHOICES)
    ga_acc_name=models.CharField(max_length=30)
    ga_bank_name=models.CharField(max_length=150)
    ga_bank_branch=models.CharField(max_length=50)
    ga_acc_no=models.BigIntegerField()
    ga_sacco_group_name=models.CharField(max_length=50)
    ga_sacco_branch_name=models.CharField(max_length=30)
    ga_mm_acc_name=models.CharField(max_length=30)
    ga_mm_provider_name=models.CharField(max_length=30)
    ga_initial_acc_balance=models.FloatField()
    ga_acc_sign=models.ForeignKey(Contributions,on_delete=models.CASCADE)
    SMS_CHOICES=(
        ('Yes','Yes'),
        ('No','No')
    )
    ga_sms_alert=models.CharField(max_length=100,choices=SMS_CHOICES)
    EMAIL_CHOICES=(
        ('Yes','Yes'),
        ('No','No')
    )
    ga_email_alert=models.CharField(max_length=15,choices=EMAIL_CHOICES)
    def _str_(self):
        return self.ga_id

class LoanType(models.Model):
    lt_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    lt_tuype=models.CharField(max_length=100)
    AMT_TYPE_CHOICES=(
        ('Based on Amount Range','Based on Amount Range'),
        ('Based on Member Saving','Based on Member Saving')
    )
    lt_amt_type=models.CharField(max_length=100,choices=AMT_TYPE_CHOICES)
    lt_mini_amt=models.FloatField()
    lt_max_amt=models.FloatField()
    INTEREST_TYPE_CHOICES=(
        ('Fixed balance reducing','Fixed balance reducing'),
        ('Balance custom','Balance custom'),
        ('Custom interest type','Custom interest type')
    )
    lt_interest_type=models.CharField(max_length=100,choices=INTEREST_TYPE_CHOICES)
    lt_interest_rate=models.CharField(max_length=100)
    INT_RATE_CHOICES=(
        ('Per day','Per day'),
        ('Per week','Per week'),
        ('Per month','Per month'),
        ('Per annum','Per annum'),
        ('For the whole loan repayment period','PFor the whole loan repayment period')
    )
    lt_interest_rate_per=models.CharField(max_length=100,choices=INT_RATE_CHOICES)
    REDUCING_CHOICES=(
        ('Yes','Yes'),
        ('No','No'),
    )
    lt_enable_reducing=models.CharField(max_length=100,choices=REDUCING_CHOICES)
    GRACE_PERIOD_CHOICES=(
        ('1 Month','1 Month'),
        ('2 Month','2 Month'),
        ('3 Month','3 Month'),
        ('4 Month','4 Month'),
        ('5 Month','5 Month'),
        ('6 Month..... 12 Month','6 Month..... 12 Month'),
        ('Custom Date','Custom Date'),
    )
    lt_grace_period=models.CharField(max_length=100,choices=GRACE_PERIOD_CHOICES)
    REPAYMENT_CHOICES=(
        ('Fixed Repayment Period','Fixed Repayment Period'),
        ('Varying Repayment Period','Varying Repayment Period')
    )
    lt_repayment_period_type=models.CharField(max_length=100,choices=REPAYMENT_CHOICES)
    lt_mini_repay_period=models.CharField(max_length=100)
    lt_max_repay_period=models.CharField(max_length=100)
    lt_fixed_repay_period=models.CharField(max_length=100)
    LATE_INTEREST_CHOICES=(
        ('Yes','Yes'),
        ('No','No'),
    )
    lt_ins_late_loan_interest=models.CharField(max_length=50,choices=LATE_INTEREST_CHOICES)
    PAY_FINE_CHOICES=(
        ('A one of fine amount per installment','A one of fine amount per installment'),
        ('A one of fine amount per installment','A one of fine amount per installment'),
        ('A one of fine amount per installment','A one of fine amount per installment'),
    )
    lt_late_loan_pay_fine=models.CharField(max_length=100,choices=PAY_FINE_CHOICES)
    FINE_TYPE_CHOICES=(
        ('Fixed','Fixed'),
        ('Percentage','Percentage'),
    )
    lt_one_off_finetype=models.CharField(max_length=50,choices=FINE_TYPE_CHOICES)
    lt_one_off_fixed_amt=models.CharField(max_length=50)
    PERCENTAGE_ON_CHOICES=(
        ('Loan installment balance','Loan installment balance'),
        ('Loan amount ','Loan amount'),
        ('Total unpaid loan','Total unpaid loan'),
        ('Loan installment interest','Loan installment interest'),
    )
    lt_one_off_percentage_amt=models.CharField(max_length=50,choices=PERCENTAGE_ON_CHOICES)
    lt_fixed_amt_charge=models.CharField(max_length=100)
    FIXAMT_FINE_CHOICES=(
        ('Daily','Daily'),
        ('Weekly','Weekly'),
        ('Monthly','Monthly'),
        ('Yearly','Yearly'),
    )
    lt_fixamt_fine_freq=models.CharField(max_length=100,choices=FIXAMT_FINE_CHOICES)
    FINE_FREQUENCY_ON_CHOICES = (
        ('Each outstanding installment', 'Each outstanding installment'),
        ('Total outstanding installment', 'Total outstanding installment'),
    )
    lt_fixamt_fine_freq_on=models.CharField(max_length=100,choices=FINE_FREQUENCY_ON_CHOICES)
    lt_fine_percentage_rate=models.CharField(max_length=100)
    FINE_FREQUENCY_ON_CHOICES=(
        ('Daily','Daily'),
        ('Weekly','Weekly'),
        ('Monthly','Monthly'),
        ('Yearly','Yearly'),
    )
    lt_fine_frequency=models.CharField(max_length=100,choices=FINE_FREQUENCY_ON_CHOICES)
    FINE_CHARGE_CHOICES=(
        ('Loan installment balance','Loan installment balance'),
        ('Loan amount ','Loan amount'),
        ('Total unpaid loan','Total unpaid loan'),
        ('Loan installment interest','Loan installment interest'),
    )
    lt_fine_charge_on=models.CharField(max_length=100,choices=FINE_CHARGE_CHOICES)
    GRANTORS_CHOICES=(
        ('Yes','Yes'),
        ('No','No'),
    )
    lt_enable_grantors=models.CharField(max_length=100,choices=GRANTORS_CHOICES)
    REQUEST_GRANTORS_CHOICES=(
        ('Every time member applying loan','Every time member applying loan'),
        ('When a member loan request exceeds maximum loan amount','When a member loan request exceeds maximum loan amount'),
    )
    lt_request_grantors=models.CharField(max_length=100,choices=REQUEST_GRANTORS_CHOICES)
    lt_mini_grantors=models.CharField(max_length=100)
    PROCESSING_FEE_CHOICES=(
        ('Yes','Yes'),
        ('No','No')
    )
    lt_loan_process_fee=models.CharField(max_length=4,choices=PROCESSING_FEE_CHOICES)
    FEE_TYPE_CHOICES=(
        ('Fixed amount','Fixed amount'),
        ('Percentage value','Percentage value')
    )
    lt_processfee_type=models.CharField(max_length=100,choices=FEE_TYPE_CHOICES)
    lt_process_fee=models.CharField(max_length=100)
    lt_process_fee_percentage=models.CharField(max_length=100)
    CHARGE_ON_CHOICES=(
        ('Total loan amount','Total loan amount'),
        ('Total loan principal plus interest','Total loan principal plus interest')
    )
    lt_charge_on=models.CharField(max_length=100,choices=CHARGE_ON_CHOICES)

class GroupRoles(models.Model):
    gr_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    gr_name=models.CharField(max_length=50)
    gr_desc=models.TextField(max_length=1000)
    def _str_(self):
        return self.gr_id
class GLCategories(models.Model):
    glc_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    GL_Ac_TYPE=(
        ('Assets','Assets'),
        ('Liabilities','Liabilities'),
        ('Equity','Equity'),
        ('Income','Income'),
        ('Expenses','Expenses'),
        ('Fine','Fine'),
    )
    glc_ac_type=models.CharField(max_length=50,choices=GL_Ac_TYPE)
    glc_line_no=models.CharField(max_length=50)
    glc_value_amt=models.CharField(max_length=50)
    glc_name=models.CharField(max_length=50)
    glc_desc=models.TextField(max_length=200)
    glc_total_credit=models.FloatField()
    glc_total_debit=models.FloatField()
    glc_balance=models.FloatField()
    def _str_(self):
        return self.glc_id

class GLEntries(models.Model):
    gle_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    LINE_NO_CHOICES=(
        ('Assets','Assets'),
        ('Liabilities','Liabilities'),
        ('Equity','Equity'),
        ('Income','Income'),
        ('Expenses','Expenses'),
        ('fine','fine'),
    )
    gle_line_no=models.CharField(max_length=100,choices=LINE_NO_CHOICES)
    gle_transaction_reference=models.CharField(max_length=100)
    gle_date=models.DateField()
    gle_time=models.TimeField()
    gle_credit_amt=models.FloatField()
    gle_debit_amt=models.FloatField()
    gle_credit_ac=models.CharField(max_length=50)
    gle_debit_ac=models.CharField(max_length=50)
    gle_posted_by_uid=models.CharField(max_length=100)
    gle_posted_date=models.DateField()
    gle_posted_time=models.TimeField()
    gle_approved_by_uid=models.CharField(max_length=100)
    gle_approved_date=models.DateField()
    gle_approved_time=models.TimeField()
    def _str_(self):
        return self.gle_id
    
class GAcManager(models.Model):
    gacm_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    gamc_fname=models.CharField(max_length=50)
    gamc_lname=models.CharField(max_length=200)
    gamc_phone_no=models.BigIntegerField()
    gamc_email=models.EmailField()
    SMS_ALERT_CHOICES=(
        ('Yes','Yes'),
        ('No','No'),
    )
    gamc_sms_alert=models.CharField(max_length=200,choices=SMS_ALERT_CHOICES)
    EMAIL_SMS_CHOICES=(
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    gamc_email_alert=models.CharField(max_length=200,choices=EMAIL_SMS_CHOICES)
    def _str_(self):
       return self.gacm_id

class LedgerType(models.Model):
    ledtype_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    TYPE_CHOICES=(
        ('General Ledger','General Ledger'),
        ('Saving Ledger','Saving Ledger'),
        ('Loans Ledger','Loans Ledger'),
    )
    ledtype=models.CharField(max_length=50,choices=TYPE_CHOICES)
    ledtype_desc=models.TextField(max_length=200)
    ledtype_total_credit=models.FloatField()
    ledtype_total_debit=models.FloatField()
    BALANCE_CHOICES=(
        (1,'Yes'),
        (0,'No'),
    )
    ledtype_balance=models.FloatField(max_length=10,choices=BALANCE_CHOICES)
    def _str_(self):
        return self.ledtype_id

class MemberRegister(models.Model):
    mr_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    FULL_NAME_CHOICES=(
        ('General Ledger','General Ledger'),
        ('Saving Ledger','Saving Ledger'),
        ('Loans  Ledger','Loans  Ledger'),
    )
    mr_full_name=models.CharField(max_length=100,choices=FULL_NAME_CHOICES)
    mr_phone_no=models.CharField(max_length=15)
    mr_email=models.EmailField()
    mr_group_role=models.ForeignKey(GAcManager,on_delete=models.CASCADE)
    mr_total_credit=models.FloatField()
    mr_total_debit=models.FloatField()
    mr_balance=models.FloatField()
    SMS_ALERT_CHOICES=(
        ('Yes','Yes'),
        ('No','No'),
    )
    mr_sms_alert=models.CharField(max_length=10,choices=SMS_ALERT_CHOICES)
    EMAIL_ALERT_CHOICES=(
        ('Yes','Yes'),
        ('No','No'),
    )
    mr_email_alert=models.CharField(max_length=10,choices=EMAIL_ALERT_CHOICES)
    def _str_(self):
        return self.mr_id
class LoanRegisterAPI(models.Model):
    lr_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
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
    def _str_(self):
        return self.lr_id

class LoanInsRegisterAPI(models.Model):
    lir_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    lir_reference=models.ForeignKey(LoanRegisterAPI,on_delete=models.CASCADE)
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

class WalletDeposits(models.Model):
    wd_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    MAKE_PAYMENT_CHOICES=(
        ('Contribution Payment','Contribution Payment'),
        ('Fine Payment','Fine Payment'),
        ('Loan Payment','Loan Payment'),
        ('Contribution Types(Savings, ) ','Contribution Types(Savings, ) '),
        ('delay fine','delay fine'),
        ('Rude behaviour','Rude behaviour'),
        ('Phone calls during meetings','Phone calls during meetings'),
        ('Miscellaneous fine','Miscellaneous fine'),
        ('Lateness to attend meeting','Lateness to attend meeting'),
        ('Absent without apology','Absent without apology'),
        ('Absent with apology','Absent with apology'),
        ('Absconding duty','Absconding duty'),
        ('List of captured Loans in the system','List of captured Loans in the system'),
        ('A text box where we capture the miscellaneous details','A text box where we capture the miscellaneous details'),
    )
    wd_makepay_for_particular=models.CharField(max_length=200,choices=MAKE_PAYMENT_CHOICES)
    wd_amt=models.FloatField()

class Depositor(models.Model):
    d_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    d_name=models.CharField(max_length=30)
    d_phone_no=models.BigIntegerField()
    d_email=models.EmailField()
    d_desc=models.TextField()
    def _str_(self):
        return self.d_id

class Accounts(models.Model):
    ac_number=models.CharField(max_length=11,primary_key=True,null=False,blank=False)
    ac_name=models.CharField(max_length=30)
    ac_member_id=models.CharField(max_length=3)
    ac_gl_cate_id=models.ForeignKey(GLCategories,on_delete=models.CASCADE)
    ac_contribution_cate_id=models.ForeignKey(Cont_categories,on_delete=models.CASCADE)
    ac_opening_date=models.DateField()
    ac_balance=models.FloatField()
    ac_last_transaction_amt=models.FloatField()
    ac_over_draft_allow=models.CharField(max_length=20)
    ac_limit_amt=models.FloatField()
    ac_last_transaction_date=models.DateField()
    def _str_(self):
        return self.ac_number

class Transactions(models.Model):
    t_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    t_date=models.DateField()
    TRANSACTION_TYPE_CHOICES=(
        ('1. Record Dividend Payments ','1.	Record Dividend Payments'),
        ('2. Record Contribution Payments ','2.	Record Contribution Payments'),
        ('3. Record Contribution Transfers ','3.	Record Contribution Transfers'),
        ('4. Record Fine Payments ','4. Record Fine Payments'),
        ('5. Record Loan Repayments','5. Record Loan Repayments'),
        ('6. Record Miscellaneous Payments','6. Record Miscellaneous Payments'),
        ('7. Record Income','7. Record Income'),
        ('8. Record Expenses','8. Record Expenses'),
    )
    t_type=models.CharField(max_length=150,choices=TRANSACTION_TYPE_CHOICES)
    t_member=models.ForeignKey(MemberRegister,on_delete=models.CASCADE)
    t_depositor=models.ForeignKey(Depositor,on_delete=models.CASCADE)
    t_expense_gl_category=models.ForeignKey(GLCategories,on_delete=models.CASCADE)
    PAY_FOR_CHOICES=(
        ('Record Contribution Payments','Record Contribution Payments'),
        ('Record Miscellaneous Payments','Record Miscellaneous Payments'),
        ('Record Income Payments','Record Income Payments'),
    )
    t_payment_for=models.CharField(max_length=50,choices=PAY_FOR_CHOICES)
    t_account=models.ForeignKey(Accounts,on_delete=models.CASCADE)
    CHANNEL_CHOICES=(
        ('Cash','Cash'),
        ('UPI','UPI'),
        ('Mobile Money','Mobile Money'),
        ('Cheque','Cheque'),
        ('Account to Account Transfer','Account to Account Transfer'),
        ('SWIFT','SWIFT'),
        ('RTGS','RTGS'),
        ('Paypal','Paypal'),
        ('Western Union','Western Union'),
        ('Deposit at Bank Account','Deposit at Bank Account'),
    )
    t_channel=models.CharField(max_length=30,choices=CHANNEL_CHOICES)
    t_desc=models.TextField(max_length=200)
    t_amount=models.FloatField()
    SMS_ALERT_CHOICES=(
        ('Yes','Yes'),
        ('No','No'),
    )
    t_sms_alert=models.CharField(max_length=5,choices=SMS_ALERT_CHOICES)
    EMAIL_ALERT_CHOICES=(
        ('Yes','Yes'),
        ('No','No'),
    )
    t_email_alert=models.CharField(max_length=5,choices=EMAIL_ALERT_CHOICES)
    t_trans_for=models.CharField(max_length=30)
    FINE_TYPE_CHOICES=(
        ('Late Payment Fine','Late Payment Fine'),
        ('Outstanding Balance Fine Date','Outstanding Balance Fine Date'),
        ('Outstanding Balance Fine','Outstanding Balance Fine'),
        ('Loan fine Deferment','Loan fine Deferment'),
    )
    t_fine_type=models.CharField(max_length=50,choices=FINE_TYPE_CHOICES)
    t_loan=models.ForeignKey(LoanRegisterAPI,on_delete=models.CASCADE)

class Ac_Transfer(models.Model):
    ata_id=models.CharField(max_length=3,primary_key=True)
    ata_transfer_date=models.DateField()
    ata_transfer_form=models.ForeignKey(Accounts,on_delete=models.CASCADE,related_name='trans_from')
    ata_transfer_to=models.ForeignKey(Accounts,on_delete=models.CASCADE,related_name='trans_to')
    ata_amt=models.FloatField()
    ata_desc=models.CharField(max_length=250)

class Contribution_Refund(models.Model):
    cr_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    cr_select_member=models.ForeignKey(MemberRegister,on_delete=models.CASCADE)
    cr_contribution_refund_from=models.ForeignKey(Contributions,on_delete=models.CASCADE)
    cr_contribution_refund_date=models.DateField()
    cr_ac_refund_from=models.ForeignKey(Accounts,on_delete=models.CASCADE)
    METHOD_CHOICES=(
        ('Cash','Cash'),
        ('UPI','UPI'),
        ('Mobile Money','Mobile Money'),
        ('Cheque','Cheque'),
        ('Account to Account Transfer','Account to Account Transfer'),
        ('SWIFT','SWIFT'),
        ('RTGS','RTGS'),
        ('Paypal','Paypal'),
        ('Western Union','Western Union'),
        ('Deposit at Bank Account','Deposit at Bank Account'),
    )
    cr_refund_method=models.CharField(max_length=100,choices=METHOD_CHOICES)
    cr_amt_refunded=models.FloatField()
    cr_desc=models.TextField()
    def _str_(self):
        return self.cr_id

class GL_ENTRIES_RECON(models.Model):
    gler_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    gler_trans_reference=models.CharField(max_length=30)
    TRANS_TABLE_NAME_CHOICES=(
        ('Transactions','Transactions'),
        ('Account to Account Transfer','Account to Account Transfer'),
        ('Contribution Refund','Contribution Refund'),
    )
    gler_trans_table_name=models.CharField(max_length=30,choices=TRANS_TABLE_NAME_CHOICES)
    gler_glenry1=models.CharField(max_length=30)
    gler_glenry2=models.CharField(max_length=30)
    gler_glenry3=models.CharField(max_length=30)
    gler_glenry4=models.CharField(max_length=30)
    gler_glenry5=models.CharField(max_length=30)
    gler_glenry6=models.CharField(max_length=30)
    gler_glenry7=models.CharField(max_length=30)
    gler_glenry8=models.CharField(max_length=30)
    gler_glenry9=models.CharField(max_length=30)
    gler_glenry10=models.CharField(max_length=30)

class Invoice(models.Model):
    i_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    i_type=models.CharField(max_length=30)
    i_contribution=models.ForeignKey(Cont_categories,on_delete=models.CASCADE)
    i_sendinvoices_to=models.ForeignKey(MemberRegister,on_delete=models.CASCADE)
    i_amt_payable=models.FloatField()
    i_invoice_date=models.DateField()
    i_invoice_due_date=models.DateField()
    i_desc=models.CharField(max_length=200)
    SMS_NOTIFICATION_CHOICES=(
        ('Yes','Yes'),
        ('No','No'),
    )
    i_send_sms_notification=models.CharField(max_length=3,choices=SMS_NOTIFICATION_CHOICES)
    EMAIL_NOTIFICATION_CHOICES=(
        ('Yes','Yes'),
        ('No','No'),
    )
    i_send_email_notification=models.CharField(max_length=3,choices=EMAIL_NOTIFICATION_CHOICES)
    i_fine_gl_category=models.ForeignKey(GLEntries,on_delete=models.CASCADE)

class Securities(models.Model):
    s_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    SECURITIES_TYPE_CHOICES=(
        ('Stock','Stock'),
        ('Asset','Asset'),
        ('Money',' Market'),
    )
    s_type=models.CharField(max_length=15,choices=SECURITIES_TYPE_CHOICES)
    s_purchase_date=models.DateField()
    s_stock_name=models.CharField(max_length=30)
    s_stock_current_shares=models.CharField(max_length=30)
    s_stock_shares_sold=models.CharField(max_length=30)
    s_stock_purchase_price=models.FloatField()
    s_stock_current_price=models.ForeignKey(Accounts,on_delete=models.CASCADE)
    s_asset_name=models.CharField(max_length=30)
    s_asset_category=models.CharField(max_length=30)
    s_asset_cost=models.FloatField()
    s_mm_investment_date=models.DateField()
    s_mm_investment_details=models.CharField(max_length=100)
    s_mm_investment_account=models.BigIntegerField()
    s_mm_amount=models.FloatField()
    s_mm_status=models.CharField(max_length=15)
    s_current_value=models.FloatField()
    s_mm_topup_amt=models.FloatField()
    s_mm_topup_date=models.DateField()
    s_mm_topup_account=models.BigIntegerField()
    s_mm_cashin_date=models.DateField()
    s_mm_cashin_account=models.FloatField()

class Asset(models.Model):
     asset_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
     asset_name=models.CharField(max_length=30)
     asset_category=models.CharField(max_length=30)
     asset_cost=models.FloatField()
     asset_desc=models.CharField(max_length=50)
     def _str_(self):
        return self.asset_id

class SecurityPurchase(models.Model):
    sp_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    sp_date=models.DateField()
    sp_stock_name=models.CharField(max_length=30)
    sp_no_shares=models.IntegerField()
    sp_asset=models.ForeignKey(Asset,on_delete=models.CASCADE)
    sp_account=models.ForeignKey(Accounts,on_delete=models.CASCADE)
    sp_price_per_shares=models.FloatField()
    sp_payment_method=models.CharField(max_length=15)
    sp_investment_institution_name=models.CharField(max_length=50)
    sp_desc=models.TextField()

class SecuritySales(models.Model):
    sl_id=models.CharField(max_length=3,primary_key=True,blank=False,null=False)
    sl_date=models.DateField()
    sl_stock_name=models.CharField(max_length=30)
    sl_no_shares_sold=models.IntegerField()
    sl_asset=models.ForeignKey(Asset,on_delete=models.CASCADE)
    sl_account=models.ForeignKey(Accounts,on_delete=models.CASCADE)
    sl_price_per_shares_asset_sale_amt=models.FloatField()
    sl_payment_method=models.CharField(max_length=15)
    sl_investment_institution_name=models.CharField(max_length=50)
    sl_desc=models.TextField()

class Upload_Contribution_Payment(models.Model):
    uploadfile_id=models.CharField(max_length=3,null=False,blank=False,primary_key=True)
    choose_file=models.FileField(upload_to='files/')
    account=models.ForeignKey(Accounts,on_delete=models.CASCADE)


class WalletRegister(models.Model):
    wallet_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    member_id=models.CharField(max_length=15)
    created_by=models.CharField(max_length=30)
    created_at=models.CharField(max_length=30)
    def _str_(self):
        return self.wallet_id

class WalletWithdrawal(models.Model):
    ww_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    wallet_balance=models.FloatField()
    amount=models.FloatField()
    wallet_id=models.ForeignKey(WalletRegister,on_delete=models.CASCADE)
    transaction_date=models.DateField()
    transaction_by=models.CharField(max_length=30)
    transaction_percentage_fee=models.FloatField()
    transaction_amount_less_plus_charge=models.FloatField()

class WithdrawalRequest(models.Model):
    wr_id=models.CharField(max_length=3,primary_key=True,null=False,blank=False)
    requested_amount=models.FloatField()
    requested_date=models.DateField()
    requested_by=models.CharField(max_length=50)
    wallet_id=models.ForeignKey(WalletRegister,on_delete=models.CASCADE)
