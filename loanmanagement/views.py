from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from loanmanagement.models import *

# Create your views here.

from datetime import datetime
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response

from loanmanagement.models import Borrowers,CostomField,Loans,LoanApplication,LoanComment
LoanDisbursedBy,LoanFees,LoanFeesMeta,LoanProduct,LoanRepayments,LoanRepaymentMethods,
LoanSchedules,LoanStatus,Savings,SavingFees,SavingsProducts,SavingsTransactions,
LoanRegister,LoanInsRegister


from drf_yasg.utils import swagger_auto_schema


from .serializers import *

from django.contrib.auth.hashers import make_password


class BorrowersView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BorrowersSerializer

    @swagger_auto_schema(responses={200: BorrowersSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        borrower= Borrowers.objects.all()
        serializer = BorrowersSerializer( borrower, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=BorrowersSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = BorrowersSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BorrowersChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BorrowersSerializer

    @swagger_auto_schema(responses={200: BorrowersSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        borrowers = get_object_or_404(Borrowers, pk=pk)
        serializer = BorrowersSerializer(borrowers)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=BorrowersSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        borrowers = get_object_or_404(Borrowers, pk=pk)
        serializer = BorrowersSerializer(borrowers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        borrowers = get_object_or_404(Borrowers, pk=pk)
        borrowers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class CostomFieldView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CostomFieldSerializer

    @swagger_auto_schema(responses={200: CostomFieldSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        costom_field= CostomField.objects.all()
        serializer = CostomFieldSerializer( costom_field, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CostomFieldSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = CostomFieldSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CostomFieldChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CostomFieldSerializer

    @swagger_auto_schema(responses={200: CostomFieldSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        costomField = get_object_or_404(CostomField, pk=pk)
        serializer = CostomFieldSerializer(costomField)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CostomFieldSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        costomField = get_object_or_404(CostomField, pk=pk)
        serializer = CostomFieldSerializer(costomField, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        costomField = get_object_or_404(CostomField, pk=pk)
        costomField.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoansView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoansSerializer

    @swagger_auto_schema(responses={200: LoansSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        loans= Loans.objects.all()
        serializer = LoansSerializer( loans, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=LoansSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = LoansSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoansChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoansSerializer

    @swagger_auto_schema(responses={200: LoansSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loans = get_object_or_404(Loans, pk=pk)
        serializer = LoansSerializer(loans)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoansSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loans = get_object_or_404(Loans, pk=pk)
        serializer = LoansSerializer(loans, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loans = get_object_or_404(Loans, pk=pk)
        loans.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views for LoanApplication
class LoanApplicationView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanApplicationSerializer

    @swagger_auto_schema(responses={200: LoanApplicationSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        loan_applications = LoanApplication.objects.all()
        serializer = LoanApplicationSerializer(loan_applications, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanApplicationSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LoanApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoanApplicationChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanApplicationSerializer

    @swagger_auto_schema(responses={200: LoanApplicationSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_applications = get_object_or_404(LoanApplication, pk=pk)
        serializer = LoanApplicationSerializer(loan_applications)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanApplicationSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_applications = get_object_or_404(LoanApplication, pk=pk)
        serializer = LoanApplicationSerializer(loan_applications, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_applications = get_object_or_404(LoanApplication, pk=pk)
        loan_applications.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Views for LoanComment
class LoanCommentView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanCommentSerializer

    @swagger_auto_schema(responses={200: LoanCommentSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        loan_comments = LoanComment.objects.all()
        serializer = LoanCommentSerializer(loan_comments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanCommentSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LoanCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanCommentChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanCommentSerializer

    @swagger_auto_schema(responses={200: LoanCommentSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_comments = get_object_or_404(LoanComment, pk=pk)
        serializer = LoanCommentSerializer(loan_comments)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanCommentSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_comments = get_object_or_404(LoanComment, pk=pk)
        serializer = LoanCommentSerializer(loan_comments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_comments = get_object_or_404(LoanComment, pk=pk)
        loan_comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class LoanDisbursedByViewset(ModelViewSet):
#     permission_classes = [permissions.AllowAny]
#     queryset = LoanDisbursedBy.objects.all()
#     serializer_class = LoanDisbursedBySerializer


class LoanDisbursedByView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanDisbursedBySerializer

    @swagger_auto_schema(responses={200: LoanDisbursedBySerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        loan_disbursed_by = LoanDisbursedBy.objects.all()
        serializer = LoanDisbursedBySerializer(loan_disbursed_by, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanDisbursedBySerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LoanDisbursedBySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanDisbursedByChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanDisbursedBySerializer

    @swagger_auto_schema(responses={200: LoanDisbursedBySerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_disbursed_by = get_object_or_404(LoanDisbursedBy, pk=pk)
        serializer = LoanDisbursedBySerializer(loan_disbursed_by)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanDisbursedBySerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_disbursed_by = get_object_or_404(LoanDisbursedBy, pk=pk)
        serializer = LoanDisbursedBySerializer(loan_disbursed_by, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_disbursed_by = get_object_or_404(LoanDisbursedBy, pk=pk)
        loan_disbursed_by.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Views for LoanFees
class LoanFeesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanFeesSerializer

    @swagger_auto_schema(responses={200: LoanFeesSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        loan_fees = LoanFees.objects.all()
        serializer = LoanFeesSerializer(loan_fees, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanFeesSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LoanFeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanFeesChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanFeesSerializer

    @swagger_auto_schema(responses={200: LoanFeesSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_fees = get_object_or_404(LoanFees, pk=pk)
        serializer = LoanFeesSerializer(loan_fees)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanFeesSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_fees = get_object_or_404(LoanFees, pk=pk)
        serializer = LoanFeesSerializer(loan_fees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_fees = get_object_or_404(LoanFees, pk=pk)
        loan_fees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Views for LoanFeesMeta
class LoanFeesMetaView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanFeesMetaSerializer

    @swagger_auto_schema(responses={200: LoanFeesMetaSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        loan_fees_meta = LoanFeesMeta.objects.all()
        serializer = LoanFeesMetaSerializer(loan_fees_meta, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanFeesMetaSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LoanFeesMetaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoanFeesMetaChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanFeesMetaSerializer

    @swagger_auto_schema(responses={200: LoanFeesMetaSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_fees_meta = get_object_or_404(LoanFeesMeta, pk=pk)
        serializer = LoanFeesMetaSerializer(loan_fees_meta)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanFeesMetaSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_fees_meta = get_object_or_404(LoanFeesMeta, pk=pk)
        serializer = LoanFeesMetaSerializer(loan_fees_meta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_fees_meta = get_object_or_404(LoanFeesMeta, pk=pk)
        loan_fees_meta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Views for LoanProduct
class LoanProductView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanProductSerializer

    @swagger_auto_schema(responses={200: LoanProductSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        loan_products = LoanProduct.objects.all()
        serializer = LoanProductSerializer(loan_products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanProductSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LoanProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanProductChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanProductSerializer

    @swagger_auto_schema(responses={200: LoanProductSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_products = get_object_or_404(LoanProduct, pk=pk)
        serializer = LoanProductSerializer(loan_products)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanProductSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_products = get_object_or_404(LoanProduct, pk=pk)
        serializer = LoanProductSerializer(loan_products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_products = get_object_or_404(LoanProduct, pk=pk)
        loan_products.delete()


# Views for LoanRepayments
class LoanRepaymentsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanRepaymentsSerializer

    @swagger_auto_schema(responses={200: LoanRepaymentsSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        loan_repayments = LoanRepayments.objects.all()
        serializer = LoanRepaymentsSerializer(loan_repayments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanRepaymentsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LoanRepaymentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanRepaymentsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanRepaymentsSerializer

    @swagger_auto_schema(responses={200: LoanRepaymentsSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_repayments = get_object_or_404(LoanRepayments, pk=pk)
        serializer = LoanRepaymentsSerializer(loan_repayments)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanRepaymentsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_repayments = get_object_or_404(LoanRepayments, pk=pk)
        serializer = LoanRepaymentsSerializer(loan_repayments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_repayments = get_object_or_404(LoanRepayments, pk=pk)
        loan_repayments.delete()


# Views for LoanRepaymentMethods
class LoanRepaymentMethodsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanRepaymentMethodsSerializer

    @swagger_auto_schema(responses={200: LoanRepaymentMethodsSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        loan_repayment_methods = LoanRepaymentMethods.objects.all()
        serializer = LoanRepaymentMethodsSerializer(loan_repayment_methods, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanRepaymentMethodsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LoanRepaymentMethodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanRepaymentMethodsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanRepaymentMethodsSerializer

    @swagger_auto_schema(responses={200: LoanRepaymentMethodsSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_repayment_methods = get_object_or_404(LoanRepaymentMethods, pk=pk)
        serializer = LoanRepaymentMethodsSerializer(loan_repayment_methods)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanRepaymentMethodsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_repayment_methods = get_object_or_404(LoanRepaymentMethods, pk=pk)
        serializer = LoanRepaymentMethodsSerializer(loan_repayment_methods, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_repayment_methods = get_object_or_404(LoanRepaymentMethods, pk=pk)
        loan_repayment_methods.delete()


# Views for LoanSchedules
class LoanSchedulesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanSchedulesSerializer

    @swagger_auto_schema(responses={200: LoanSchedulesSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        loan_schedules = LoanSchedules.objects.all()
        serializer = LoanSchedulesSerializer(loan_schedules, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanSchedulesSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LoanSchedulesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoanSchedulesChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanSchedulesSerializer

    @swagger_auto_schema(responses={200: LoanSchedulesSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_schedules = get_object_or_404(LoanSchedules, pk=pk)
        serializer = LoanSchedulesSerializer(loan_schedules)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanSchedulesSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_schedules = get_object_or_404(LoanSchedules, pk=pk)
        serializer = LoanSchedulesSerializer(loan_schedules, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_schedules = get_object_or_404(LoanSchedules, pk=pk)
        loan_schedules.delete()


class LoanStatusView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanStatusSerializer

    @swagger_auto_schema(responses={200: LoanStatusSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        loan_status = LoanStatus.objects.all()
        serializer = LoanStatusSerializer(loan_status, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanStatusSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LoanStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class LoanStatusChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanStatusSerializer

    @swagger_auto_schema(responses={200: LoanStatusSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_status = get_object_or_404(LoanStatus, pk=pk)
        serializer = LoanStatusSerializer(loan_status)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanStatusSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_status = get_object_or_404(LoanStatus, pk=pk)
        serializer = LoanStatusSerializer(loan_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_status = get_object_or_404(LoanStatus, pk=pk)
        loan_status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views for Savings
class SavingsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SavingsSerializer

    @swagger_auto_schema(responses={200: SavingsSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        savings = Savings.objects.all()
        serializer = SavingsSerializer(savings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SavingsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = SavingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SavingsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SavingsSerializer

    @swagger_auto_schema(responses={200: SavingsSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        savings = get_object_or_404(Savings, pk=pk)
        serializer = SavingsSerializer(savings)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SavingsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        savings = get_object_or_404(Savings, pk=pk)
        serializer = SavingsSerializer(savings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        savings = get_object_or_404(Savings, pk=pk)
        savings.delete()


# Views for SavingFees
class SavingFeesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SavingFeesSerializer

    @swagger_auto_schema(responses={200: SavingFeesSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        saving_fees = SavingFees.objects.all()
        serializer = SavingFeesSerializer(saving_fees, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SavingFeesSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = SavingFeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SavingFeesChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SavingFeesSerializer

    @swagger_auto_schema(responses={200: SavingFeesSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        saving_fees = get_object_or_404(SavingFees, pk=pk)
        serializer = SavingFeesSerializer(saving_fees)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SavingFeesSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        saving_fees = get_object_or_404(SavingFees, pk=pk)
        serializer = SavingFeesSerializer(saving_fees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        saving_fees = get_object_or_404(SavingFees, pk=pk)
        saving_fees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Views for SavingsProducts
class SavingsProductsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SavingsProductsSerializer

    @swagger_auto_schema(responses={200: SavingsProductsSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        savings_products = SavingsProducts.objects.all()
        serializer = SavingsProductsSerializer(savings_products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SavingsProductsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = SavingsProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SavingsProductsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SavingsProductsSerializer

    @swagger_auto_schema(responses={200: SavingsProductsSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        savings_products = get_object_or_404(SavingsProducts, pk=pk)
        serializer = SavingsProductsSerializer(savings_products)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SavingsProductsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        savings_products = get_object_or_404(SavingsProducts, pk=pk)
        serializer = SavingsProductsSerializer(savings_products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        savings_products = get_object_or_404(SavingsProducts, pk=pk)
        savings_products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Views for SavingsTransactions
class SavingsTransactionsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SavingsTransactionsSerializer

    @swagger_auto_schema(responses={200: SavingsTransactionsSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        savings_transactions = SavingsTransactions.objects.all()
        serializer = SavingsTransactionsSerializer(savings_transactions, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SavingsTransactionsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = SavingsTransactionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SavingsTransactionsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SavingsTransactionsSerializer

    @swagger_auto_schema(responses={200: SavingsTransactionsSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        savings_transactions = get_object_or_404(SavingsTransactions, pk=pk)
        serializer = SavingsTransactionsSerializer(savings_transactions)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SavingsTransactionsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        savings_transactions = get_object_or_404(SavingsTransactions, pk=pk)
        serializer = SavingsTransactionsSerializer(savings_transactions, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        savings_transactions = get_object_or_404(SavingsTransactions, pk=pk)
        savings_transactions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Views for LoanRegister
class LoanRegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanRegisterSerializer

    @swagger_auto_schema(responses={200: LoanRegisterSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        loan_register = LoanRegister.objects.all()
        serializer = LoanRegisterSerializer(loan_register, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanRegisterSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LoanRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanRegisterChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanRegisterSerializer

    @swagger_auto_schema(responses={200: LoanRegisterSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_register = get_object_or_404(LoanRegister, pk=pk)
        serializer = LoanRegisterSerializer(loan_register)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanRegisterSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_register = get_object_or_404(LoanRegister, pk=pk)
        serializer = LoanRegisterSerializer(loan_register, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_register = get_object_or_404(LoanRegister, pk=pk)
        loan_register.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Views for LoanInsRegister
class LoanInsRegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanInsRegisterSerializer

    @swagger_auto_schema(responses={200: LoanInsRegisterSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        loan_ins_register = LoanInsRegister.objects.all()
        serializer = LoanInsRegisterSerializer(loan_ins_register, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanInsRegisterSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializer = LoanInsRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoanInsRegisterChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanInsRegisterSerializer

    @swagger_auto_schema(responses={200: LoanInsRegisterSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_ins_register = get_object_or_404(LoanInsRegister, pk=pk)
        serializer = LoanInsRegisterSerializer(loan_ins_register)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanInsRegisterSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_ins_register = get_object_or_404(LoanInsRegister, pk=pk)
        serializer = LoanInsRegisterSerializer(loan_ins_register, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_ins_register = get_object_or_404(LoanInsRegister, pk=pk)
        loan_ins_register.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




