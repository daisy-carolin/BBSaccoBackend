from django.urls import path
from . import views
from .models import*

urlpatterns = [
    path('borrowers', views.BorrowersView.as_view(), name='borrowers_api'),
    path('costom_field', views.CostomFieldView.as_view(), name='costom_field_api'),
    path('loans', views.LoansView.as_view(), name='loans_api'),
    path('loan_application', views.LoanApplicationView.as_view(), name='loan_application_api'),
    path('loan_comment', views.LoanCommentView.as_view(), name='loan_comment_api'),
    path('loan_disbursed_by', views.LoanDisbursedByView.as_view(), name='loan_disbursed_by_api'),
    path('loan_fees', views.LoanFeesView.as_view(), name='loan_fees_api'),
    path('loan_fees_meta', views.LoanFeesMetaView.as_view(), name='loan_fees_meta_api'),
    path('loan_product', views.LoanProductView.as_view(), name='loan_product_api'),
    path('loan_repayments', views.LoanRepaymentsView.as_view(), name='loan_repayments_api'),
    path('loan_repayment_methods', views.LoanRepaymentMethodsView.as_view(), name='loan_repayment_methods_api'),
    path('loan_schedules', views.LoanSchedulesView.as_view(), name='loan_schedules_api'),
    path('loan_status', views.LoanStatusView.as_view(), name='loan_status_api'),
    path('savings', views.SavingsView.as_view(), name='savings_api'),
    path('saving_fees', views.SavingFeesView.as_view(), name='saving_fees_api'),
    path('savings_products', views.SavingsProductsView.as_view(), name='savings_products_api'),
    path('savings_transactions', views.SavingsTransactionsView.as_view(), name='savings_transactions_api'),
    path('loan_register', views.LoanRegisterView.as_view(), name='loan_register_api'),
    path('loan_ins_register', views.LoanInsRegisterView.as_view(), name='loan_ins_register_api'),
]
