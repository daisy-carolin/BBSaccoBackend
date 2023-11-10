from django.urls import path
from . import views
from .borrowers import *
from .branches import *
from .add_borrowers import *


urlpatterns = [
    path('borrowers', views.Borrowers1View.as_view(), name='borrowers_api'),
    path('borrowers_update/<int:pk>/', views.Borrowers1ChangeView.as_view(), name='borrowers_update'),
    path('branch', views.BranchView.as_view(), name='branch_api'),
    path('branch/<int:pk>/', views.BranchChangeView.as_view(), name='branch_update'),
    path('branch_change', views.AddUserInBranchView.as_view(), name='branch_change_api'),
    path('branch_change_update/<int:pk>/', views.AddUserInBranchChangeView.as_view(), name='branch_change_update'),
    path('add_user_in_branch', views.AddUserInBranchView.as_view(), name='add_user_in_branch_api'),
    path('add_user_in_branch_update/<int:pk>/', views.AddUserInBranchChangeView.as_view(), name='add_user_in_branch_update'),

]