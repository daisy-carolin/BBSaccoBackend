from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .models import*

# router = DefaultRouter()
# router.register(r'loan_disbursed_by', views.LoanDisbursedByViewset)

urlpatterns = [
    path('borrowers', views.BorrowersView.as_view(), name='borrowers_api'),
    path('borrowers_update/<int:pk>/', views.BorrowersChangeView.as_view(), name='borrowers_update'),
    path('costom_field', views.CostomFieldView.as_view(), name='costom_field_api'),
    path('costom_field_update/<int:pk>/', views.CostomFieldChangeView.as_view(), name='costom_field_update'),
    path('loans', views.LoansView.as_view(), name='loans_api'),
    path('loans/<int:pk>/', views.LoansChangeView.as_view(), name='loans_update'),
    path('loan_application', views.LoanApplicationView.as_view(), name='loan_application_api'),
    path('loan_application/<int:pk>/', views.LoanApplicationChangeView.as_view(), name='loan_application_update'),
    path('loan_comment', views.LoanCommentView.as_view(), name='loan_comment_api'),
    path('loan_comment/<int:pk>/', views.LoanCommentChangeView.as_view(), name='loan_comment_update'),
    path('loan_disbursed_by/<int:pk>/', views.LoanDisbursedByChangeView.as_view(), name='loan_disbursed_by_update'),
    path('loan_disbursed_by', views.LoanDisbursedByView.as_view(), name='loan_disbursed_by_api'),
    path('loan_fees', views.LoanFeesView.as_view(), name='loan_fees_api'),
    path('loan_fees/<int:pk>/', views.LoanFeesChangeView.as_view(), name='loan_fees_update'),
    path('loan_fees_meta', views.LoanFeesMetaView.as_view(), name='loan_fees_meta_api'),
    path('loan_fees_meta/<int:pk>/', views.LoanFeesMetaChangeView.as_view(), name='loan_fees_meta_update'),
    path('loan_product/<int:pk>/', views.LoanProductChangeView.as_view(), name='loan_product_update'),
    path('loan_product', views.LoanProductView.as_view(), name='loan_product_api'),
    path('loan_repayments/<int:pk>/', views.LoanRepaymentsChangeView.as_view(), name='loan_repayments_update'),
    path('loan_repayments', views.LoanRepaymentsView.as_view(), name='loan_repayments_api'),
    path('loan_repayment_methods/<int:pk>/', views.LoanRepaymentMethodsChangeView.as_view(), name='loan_repayment_methods_update'),
    path('loan_repayment_methods', views.LoanRepaymentMethodsView.as_view(), name='loan_repayment_methods_api'),
    path('loan_schedules', views.LoanSchedulesView.as_view(), name='loan_schedules_api'),
    path('loan_schedules/<int:pk>/', views.LoanSchedulesChangeView.as_view(), name='loan_schedules_update'),
    path('loan_status', views.LoanStatusView.as_view(), name='loan_status_api'),
    path('loan_status/<int:pk>/', views.LoanStatusChangeView.as_view(), name='loan_status_update'),
    path('savings', views.SavingsView.as_view(), name='savings_api'),
    path('savings/<int:pk>/', views.SavingsChangeView.as_view(), name='savings_update'),
    path('saving_fees', views.SavingFeesView.as_view(), name='saving_fees_api'),
    path('saving_fees/<int:pk>/', views.SavingFeesChangeView.as_view(), name='saving_fees_update'),
    path('savings_products/<int:pk>/', views.SavingsProductsChangeView.as_view(), name='savings_products_update'),
    path('savings_products', views.SavingsProductsView.as_view(), name='savings_products_api'),
    path('savings_transactions/<int:pk>/', views.SavingsTransactionsChangeView.as_view(), name='savings_transactions_update'),
    path('savings_transactions', views.SavingsTransactionsView.as_view(), name='savings_transactions_api'),
    path('loan_register/<int:pk>/', views.LoanRegisterChangeView.as_view(), name='loan_register_update'),
    path('loan_register', views.LoanRegisterView.as_view(), name='loan_register_api'),
    path('loan_ins_register', views.LoanInsRegisterView.as_view(), name='loan_ins_register_api'),
    path('loan_ins_register/<int:pk>/', views.LoanInsRegisterChangeView.as_view(), name='loan_ins_register_update'),

]
