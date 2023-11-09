from rest_framework import serializers, fields

from .models import *

class BorrowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowers
        fields = "__all__"


class CostomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostomField
        fields = "__all__"


class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = "__all__"


class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = "__all__"


class LoanCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanComment
        fields = "__all__"


class  LoanDisbursedBySerializer(serializers.ModelSerializer):
    class Meta:
        model =  LoanDisbursedBy
        fields = "__all__"


class  LoanFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model =  LoanFees
        fields = "__all__"


class  LoanFeesMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model =  LoanFeesMeta
        fields = "__all__"


class  LoanProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =  LoanProduct
        fields = "__all__"


class LoanRepaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRepayments
        fields = "__all__"



class LoanRepaymentMethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRepaymentMethods
        fields = "__all__"


class LoanSchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanSchedules
        fields = "__all__"


class LoanStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanStatus
        fields = "__all__"

    


class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields = "__all__"
        

class SavingFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingFees
        fields = "__all__"


class SavingsProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  SavingsProducts
        fields = "__all__"


class SavingsTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  SavingsTransactions
        fields = "__all__"


class LoanRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  LoanRegister
        fields = "__all__"


class LoanInsRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  LoanInsRegister
        fields = "__all__"

