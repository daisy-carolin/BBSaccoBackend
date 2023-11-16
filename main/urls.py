from django.urls import path
from . import views

urlpatterns = [
    path('cont_categories', views.Cont_categoriesView.as_view(), name='cont_categories_api'),
    path('cont_categories_update/<int:pk>/', views.Cont_categoriesChangeView.as_view(), name='cont_categories_update'),

    path('contributions', views.ContributionsView.as_view(), name='contributions_api'),
    path('contributions_update/<int:pk>/', views.ContributionsChangeView.as_view(), name='contributions_update'),

    path('groupa_accounts', views.GroupAaccountsView.as_view(), name='groupa_accounts_api'),
    path('groupa_accounts_update/<int:pk>/', views.GroupAaccountsChangeView.as_view(), name='groupa_accounts_update'),

    path('gl_categories', views.GLCategoriesView.as_view(), name='gl_categories_api'),
    path('gl_categories_update/<int:pk>/', views.GLCategoriesChangeView.as_view(), name='gl_categories_update'),

    path('gl_entries', views.GLEntriesView.as_view(), name='gl_entries_api'),
    path('gl_entries_update/<int:pk>/', views.GLEntriesChangeView.as_view(), name='gl_entries_update'),

    path('gac_manager', views.GAcManagerView.as_view(), name='gac_manager_api'),
    path('gac_manager_update/<int:pk>/', views.GAcManagerChangeView.as_view(), name='gac_manager_update'),

    path('ledger_type', views.LedgerTypeView.as_view(), name='ledger_type_api'),
    path('ledger_type_update/<int:pk>/', views.LedgerTypeChangeView.as_view(), name='ledger_type_update'),

    path('member_register', views.MemberRegisterView.as_view(), name='member_register_api'),
    path('member_register_update/<int:pk>/', views.MemberRegisterChangeView.as_view(), name='member_register_update'),

    path('loan_register', views.LoanRegisterAPIView.as_view(), name='loan_register_api'),
    path('loan_register_update/<int:pk>/', views.LoanRegisterAPIChangeView.as_view(), name='loan_register_update'),

    path('loan_ins_register', views.LoanInsRegisterAPIView.as_view(), name='loan_ins_register_api'),
    path('loan_ins_register_update/<int:pk>/', views.LoanInsRegisterAPIChangeView.as_view(), name='loan_ins_register_update'),

    path('wallet_deposits', views.WalletDepositsView.as_view(), name='wallet_deposits_api'),
    path('wallet_deposits_update/<int:pk>/', views.WalletDepositsChangeView.as_view(), name='wallet_deposits_update'),

    path('depositor', views.DepositorView.as_view(), name='depositor_api'),
    path('depositor_update/<int:pk>/', views.DepositorChangeView.as_view(), name='depositor_update'),

    path('accounts', views.AccountsView.as_view(), name='accounts_api'),
    path('accounts_update/<int:pk>/', views.AccountsChangeView.as_view(), name='accounts_update'),

    path('transactions', views.TransactionsView.as_view(), name='transactions_api'),
    path('transactions_update/<int:pk>/', views.TransactionsChangeView.as_view(), name='transactions_update'),

    path('ac_transfer', views.Ac_TransferView.as_view(), name='ac_transfer_api'),
    path('ac_transfer_update/<int:pk>/', views.Ac_TransferChangeView.as_view(), name='ac_transfer_update'),

    path('contribution_refund', views.Contribution_RefundView.as_view(), name='contribution_refund_api'),
    path('contribution_refund_update/<int:pk>/', views.Contribution_RefundChangeView.as_view(), name='contribution_refund_update'),

    path('gl_entries_recon', views.GL_ENTRIES_RECONView.as_view(), name='gl_entries_recon_api'),
    path('gl_entries_recon_update/<int:pk>/', views.GL_ENTRIES_RECONChangeView.as_view(), name='gl_entries_recon_update'),

    path('invoice', views.InvoiceView.as_view(), name='invoice_api'),
    path('invoice_update/<int:pk>/', views.InvoiceChangeView.as_view(), name='invoice_update'),

    path('securities', views.SecuritiesView.as_view(), name='securities_api'),
    path('securities_update/<int:pk>/', views.SecuritiesChangeView.as_view(), name='securities_update'),

    path('asset', views.AssetView.as_view(), name='asset_api'),
    path('asset_update/<int:pk>/', views.AssetChangeView.as_view(), name='asset_update'),

    path('security_purchase', views.SecurityPurchaseView.as_view(), name='security_purchase_api'),
    path('security_purchase_update/<int:pk>/', views.SecurityPurchaseChangeView.as_view(), name='security_purchase_update'),

    path('security_sales', views.SecuritySalesView.as_view(), name='security_sales_api'),
    path('security_sales_update/<int:pk>/', views.SecuritySalesChangeView.as_view(), name='security_sales_update'),

    path('upload_contribution_payment', views.Upload_Contribution_PaymentView.as_view(), name='upload_contribution_payment_api'),
    path('upload_contribution_payment_update/<int:pk>/', views.Upload_Contribution_PaymentChangeView.as_view(), name='upload_contribution_payment_update'),

    path('wallet_withdrawal', views.WalletWithdrawalView.as_view(), name='wallet_withdrawal_api'),
    path('wallet_withdrawal_update/<int:pk>/', views.WalletWithdrawalChangeView.as_view(), name='wallet_withdrawal_update'),

    path('withdrawal_request', views.WithdrawalRequestView.as_view(), name='withdrawal_request_api'),
    path('withdrawal_request_update/<int:pk>/', views.WithdrawalRequestChangeView.as_view(), name='withdrawal_request_update'),

    
]
