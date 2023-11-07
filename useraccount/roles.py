from django.db import models

class Role(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False,unique=True)
    slug=models.SlugField(max_length=250,blank=True,null=True,editable=False)
    #Borrowers
    view_borrowers=models.BooleanField(default=False)
    update_borrowers=models.BooleanField(default=False)
    delete_borrowers=models.BooleanField(default=False)
    create_borrowers=models.BooleanField(default=False)
    approve_borrowers=models.BooleanField(default=False)
    blacklist_borrowers=models.BooleanField(default=False)
    manage_borrowers_groups=models.BooleanField(default=False)
    #Loans
    create_loans = models.BooleanField(default=False)
    update_loans = models.BooleanField(default=False)
    delete_loans = models.BooleanField(default=False)
    view_loans = models.BooleanField(default=False)
    loan_products = models.BooleanField(default=False)
    loan_fees = models.BooleanField(default=False)
    loan_schedule = models.BooleanField(default=False)
    approve_loans = models.BooleanField(default=False)
    disburse_loans = models.BooleanField(default=False)
    withdraw_loans = models.BooleanField(default=False)
    write_off_loans = models.BooleanField(default=False)
    reschedule_loans = models.BooleanField(default=False)
    create_guarantor = models.BooleanField(default=False)
    update_guarantor = models.BooleanField(default=False)
    guarantor_savings = models.BooleanField(default=False)
    use_loan_calculator = models.BooleanField(default=False)
    #Repayment
    view_repayments = models.BooleanField(default=False)
    create_repayments = models.BooleanField(default=False)
    delete_repayments = models.BooleanField(default=False)
    update_repayments = models.BooleanField(default=False)
    #branches
    view_branches = models.BooleanField(default=False)
    update_branches = models.BooleanField(default=False)
    delete_branches = models.BooleanField(default=False)
    create_branches = models.BooleanField(default=False)
    #Expenses
    view_expenses = models.BooleanField(default=False)
    update_expenses = models.BooleanField(default=False)
    delete_expenses = models.BooleanField(default=False)
    create_expenses = models.BooleanField(default=False)
    #  Other Income
    view_other_income  = models.BooleanField(default=False)
    update_other_income  = models.BooleanField(default=False)
    delete_other_income  = models.BooleanField(default=False)
    create_other_income  = models.BooleanField(default=False)
    # Collateral
    view_collateral = models.BooleanField(default=False)
    update_collateral = models.BooleanField(default=False)
    delete_collateral = models.BooleanField(default=False)
    create_collateral = models.BooleanField(default=False)
    #Reports
    reports=models.BooleanField(default=False)
    #Communication
    create_communication = models.BooleanField(default=False)
    delete_communication = models.BooleanField(default=False)
    #Custom Fields
    view_custom_fields = models.BooleanField(default=False)
    create_custom_fields = models.BooleanField(default=False)
    custom_fields = models.BooleanField(default=False)
    delete_custom_fields = models.BooleanField(default=False)
    #Users
    view_users=models.BooleanField(default=False)
    create_users=models.BooleanField(default=False)
    update_users=models.BooleanField(default=False)
    delete_users=models.BooleanField(default=False)
    manage_role=models.BooleanField(default=False)
    #settings
    settings=models.BooleanField(default=False)
    #audit trail
    audit_trail = models.BooleanField(default=False)
    #savings
    create_savings = models.BooleanField(default=False)
    update_savings = models.BooleanField(default=False)
    delete_savings = models.BooleanField(default=False)
    create_savings_transaction = models.BooleanField(default=False)
    update_savings_transaction = models.BooleanField(default=False)
    delete_savings_transaction = models.BooleanField(default=False)
    view_savings = models.BooleanField(default=False)
    view_savings_transaction = models.BooleanField(default=False)
    manage_savings_products = models.BooleanField(default=False)
    manage_savings_fees = models.BooleanField(default=False)
    # branches
    view_branches = models.BooleanField(default=False)
    update_branches = models.BooleanField(default=False)
    delete_branches = models.BooleanField(default=False)
    create_branches = models.BooleanField(default=False)
    assign_users = models.BooleanField(default=False)

    '''
        Next We  Permission fields we add later.....
        '''

