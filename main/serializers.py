from rest_framework import serializers, fields

from .models import *


class Cont_categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cont_categories
        fields = "__all__"


class ContributionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributions
        fields = "__all__"


class GroupAaccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupAaccounts
        fields = "__all__"


class LoanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model =LoanType
        fields = "__all__"


class GroupRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupRoles
        fields = "__all__"


class GLCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GLCategories
        fields = "__all__"


class GLEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GLEntries
        fields = "__all__"


class GAcManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GAcManager
        fields = "__all__"


class LedgerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerType
        fields = "__all__"


class MemberRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberRegister
        fields = "__all__"


class LoanRegisterAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRegisterAPI
        fields = "__all__"


class LoanInsRegisterAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanInsRegisterAPI
        fields = "__all__"


class WalletDepositsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletDeposits
        fields = "__all__"


class  DepositorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depositor
        fields = "__all__"


class  AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = "__all__"


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"


class Ac_TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ac_Transfer
        fields = "__all__"


class Contribution_RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution_Refund
        fields = "__all__"


class GL_ENTRIES_RECONSerializer(serializers.ModelSerializer):
    class Meta:
        model = GL_ENTRIES_RECON
        fields = "__all__"


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"


class SecuritiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Securities
        fields = "__all__"


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"


class SecurityPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityPurchase
        fields = "__all__"


class SecuritySalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecuritySales
        fields = "__all__"


class Upload_Contribution_PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload_Contribution_Payment
        fields = "__all__"


class WalletWithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletWithdrawal
        fields = "__all__"


class WithdrawalRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = WithdrawalRequest
        fields = "__all__"


class WalletRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model =WalletRegister
        fields = "__all__"