from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from main.models import GroupRoles, LoanType

from main.serializers import *
# Create your views here.

from datetime import datetime
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models  import *

from django.contrib.auth.hashers import make_password


class Cont_categoriesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Cont_categoriesSerializer

    @swagger_auto_schema(responses={200: Cont_categoriesSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        cont_categories= Cont_categories.objects.all()
        serializer = Cont_categoriesSerializer( cont_categories, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=Cont_categoriesSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = Cont_categoriesSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class Cont_categoriesChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Cont_categoriesSerializer

    @swagger_auto_schema(responses={200: Cont_categoriesSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        cont_categories = get_object_or_404(Cont_categories, pk=pk)
        serializer = Cont_categoriesSerializer(cont_categories)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=Cont_categoriesSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        cont_categories= get_object_or_404(Cont_categories, pk=pk)
        serializer = Cont_categoriesSerializer(cont_categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        cont_categories = get_object_or_404(Cont_categories, pk=pk)
        cont_categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContributionsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ContributionsSerializer

    @swagger_auto_schema(responses={200: ContributionsSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        contributions= Contributions.objects.all()
        serializer = ContributionsSerializer( contributions, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ContributionsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = ContributionsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ContributionsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ContributionsSerializer

    @swagger_auto_schema(responses={200: ContributionsSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        contributions = get_object_or_404(Contributions, pk=pk)
        serializer = ContributionsSerializer(contributions)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ContributionsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        contributions= get_object_or_404(Contributions, pk=pk)
        serializer = ContributionsSerializer(contributions, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        contributions = get_object_or_404(Contributions, pk=pk)
        contributions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class GroupAaccountsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GroupAaccountsSerializer

    @swagger_auto_schema(responses={200: GroupAaccountsSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        group_aaccounts= GroupAaccounts.objects.all()
        serializer = GroupAaccountsSerializer( group_aaccounts, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=GroupAaccountsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = GroupAaccountsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupAaccountsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GroupAaccountsSerializer

    @swagger_auto_schema(responses={200: GroupAaccountsSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        group_aaccounts = get_object_or_404(GroupAaccounts, pk=pk)
        serializer = GroupAaccountsSerializer(group_aaccounts)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=GroupAaccountsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        group_aaccounts= get_object_or_404(GroupAaccounts, pk=pk)
        serializer = GroupAaccountsSerializer(group_aaccounts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        group_aaccounts = get_object_or_404(GroupAaccounts, pk=pk)
        group_aaccounts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class LoanTypeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanTypeSerializer

    @swagger_auto_schema(responses={200: LoanTypeSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        loan_type= LoanType.objects.all()
        serializer = LoanTypeSerializer( loan_type, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=LoanTypeSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = LoanTypeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanTypeChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanTypeSerializer

    @swagger_auto_schema(responses={200: LoanTypeSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_type = get_object_or_404(LoanType, pk=pk)
        serializer = LoanTypeSerializer(loan_type)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanTypeSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_type= get_object_or_404(LoanType, pk=pk)
        serializer = LoanTypeSerializer(loan_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_type = get_object_or_404(LoanType, pk=pk)
        loan_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class GLCategoriesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GLCategoriesSerializer

    @swagger_auto_schema(responses={200: GLCategoriesSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        gl_categories= GLCategories.objects.all()
        serializer = GLCategoriesSerializer( gl_categories, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=GLCategoriesSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = GLCategoriesSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class GLCategoriesChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GLCategoriesSerializer

    @swagger_auto_schema(responses={200: GLCategoriesSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        gl_categories = get_object_or_404(GLCategories, pk=pk)
        serializer = GLCategoriesSerializer(gl_categories)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=GLCategoriesSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        gl_categories= get_object_or_404(GLCategories, pk=pk)
        serializer = GLCategoriesSerializer(gl_categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        gl_categories = get_object_or_404(GLCategories, pk=pk)
        gl_categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class GroupRolesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GroupRolesSerializer

    @swagger_auto_schema(responses={200: GroupRolesSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        group_roles= GroupRoles.objects.all()
        serializer = GroupRolesSerializer( group_roles, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=GroupRolesSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = GroupRolesSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupRolesChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GroupRolesSerializer

    @swagger_auto_schema(responses={200: GroupRolesSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        group_roles = get_object_or_404(GroupRoles, pk=pk)
        serializer = GroupRolesSerializer(group_roles)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=GroupRolesSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        group_roles= get_object_or_404(GroupRoles, pk=pk)
        serializer = GroupRolesSerializer(group_roles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        group_roles = get_object_or_404(GroupRoles, pk=pk)
        group_roles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GLEntriesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GLEntriesSerializer

    @swagger_auto_schema(responses={200: GLEntriesSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        gl_entries= GLEntries.objects.all()
        serializer = GLEntriesSerializer( gl_entries, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=GLEntriesSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = GLEntriesSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class GLEntriesChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GLEntriesSerializer

    @swagger_auto_schema(responses={200: GLEntriesSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        gl_entries = get_object_or_404(GLEntries, pk=pk)
        serializer = GLEntriesSerializer(gl_entries)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=GLEntriesSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        gl_entries= get_object_or_404(GLEntries, pk=pk)
        serializer = GLEntriesSerializer(gl_entries, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        gl_entries = get_object_or_404(GLEntries, pk=pk)
        gl_entries.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GAcManagerView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GAcManagerSerializer

    @swagger_auto_schema(responses={200: GAcManagerSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        ga_manager= GAcManager.objects.all()
        serializer = GAcManagerSerializer( ga_manager, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=GAcManagerSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = GAcManagerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class GAcManagerChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GAcManagerSerializer

    @swagger_auto_schema(responses={200: GAcManagerSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        ga_manager = get_object_or_404(GAcManager, pk=pk)
        serializer = GAcManagerSerializer(ga_manager)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=GAcManagerSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        ga_manager= get_object_or_404(GAcManager, pk=pk)
        serializer = GAcManagerSerializer(ga_manager, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        ga_manager = get_object_or_404(GAcManager, pk=pk)
        ga_manager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class LedgerTypeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LedgerTypeSerializer

    @swagger_auto_schema(responses={200: LedgerTypeSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        ledger_type= LedgerType.objects.all()
        serializer = LedgerTypeSerializer( ledger_type, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=LedgerTypeSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = LedgerTypeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class LedgerTypeChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LedgerTypeSerializer

    @swagger_auto_schema(responses={200: LedgerTypeSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        ledger_type = get_object_or_404(LedgerType, pk=pk)
        serializer = LedgerTypeSerializer(ledger_type)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LedgerTypeSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        ledger_type= get_object_or_404(LedgerType, pk=pk)
        serializer = LedgerTypeSerializer(ledger_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        ledger_type = get_object_or_404(LedgerType, pk=pk)
        ledger_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class MemberRegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MemberRegisterSerializer

    @swagger_auto_schema(responses={200: MemberRegisterSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        member_register= MemberRegister.objects.all()
        serializer = MemberRegisterSerializer( member_register, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=MemberRegisterSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = MemberRegisterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class MemberRegisterChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MemberRegisterSerializer

    @swagger_auto_schema(responses={200: MemberRegisterSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        member_register = get_object_or_404(MemberRegister, pk=pk)
        serializer = MemberRegisterSerializer(member_register)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=MemberRegisterSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        member_register= get_object_or_404(MemberRegister, pk=pk)
        serializer = MemberRegisterSerializer(member_register, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        member_register = get_object_or_404(MemberRegister, pk=pk)
        member_register.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class LoanRegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanRegisterAPISerializer

    @swagger_auto_schema(responses={200: LoanRegisterAPISerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        loan_register= LoanRegisterAPI.objects.all()
        serializer = LoanRegisterAPISerializer( loan_register, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=LoanRegisterAPISerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = LoanRegisterAPISerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanRegisterAPIChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanRegisterAPISerializer

    @swagger_auto_schema(responses={200: LoanRegisterAPISerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_register = get_object_or_404(LoanRegisterAPI, pk=pk)
        serializer = LoanRegisterAPISerializer(loan_register)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanRegisterAPISerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_register= get_object_or_404(LoanRegisterAPI, pk=pk)
        serializer = LoanRegisterAPISerializer(loan_register, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_register = get_object_or_404(LoanRegisterAPI, pk=pk)
        loan_register.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class LoanInsRegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanInsRegisterAPISerializer

    @swagger_auto_schema(responses={200: LoanInsRegisterAPISerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        loan_ins_register= LoanInsRegisterAPI.objects.all()
        serializer = LoanInsRegisterAPISerializer( loan_ins_register, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=LoanInsRegisterAPISerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = LoanInsRegisterAPISerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanInsRegisterAPIChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanInsRegisterAPISerializer

    @swagger_auto_schema(responses={200: LoanInsRegisterAPISerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        loan_ins_register = get_object_or_404(LoanInsRegisterAPI, pk=pk)
        serializer = LoanInsRegisterAPISerializer(loan_ins_register)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=LoanInsRegisterAPISerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        loan_ins_register= get_object_or_404(LoanInsRegisterAPI, pk=pk)
        serializer = LoanInsRegisterAPISerializer(loan_ins_register, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        loan_ins_register = get_object_or_404(LoanInsRegisterAPI, pk=pk)
        loan_ins_register.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class WalletDepositsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = WalletDepositsSerializer

    @swagger_auto_schema(responses={200: WalletDepositsSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        wallet_deposits= WalletDeposits.objects.all()
        serializer = WalletDepositsSerializer( wallet_deposits, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=WalletDepositsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = WalletDepositsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class WalletDepositsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = WalletDepositsSerializer

    @swagger_auto_schema(responses={200: WalletDepositsSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        wallet_deposits = get_object_or_404(WalletDeposits, pk=pk)
        serializer = WalletDepositsSerializer(wallet_deposits)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=WalletDepositsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        wallet_deposits= get_object_or_404(WalletDeposits, pk=pk)
        serializer = WalletDepositsSerializer(wallet_deposits, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        wallet_deposits = get_object_or_404(WalletDeposits, pk=pk)
        wallet_deposits.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DepositorView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DepositorSerializer

    @swagger_auto_schema(responses={200: DepositorSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        depositor= Depositor.objects.all()
        serializer = DepositorSerializer( depositor, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=DepositorSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = DepositorSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class DepositorChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DepositorSerializer

    @swagger_auto_schema(responses={200: DepositorSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        depositor = get_object_or_404(Depositor, pk=pk)
        serializer = DepositorSerializer(depositor)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=DepositorSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        depositor= get_object_or_404(Depositor, pk=pk)
        serializer = DepositorSerializer(depositor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        depositor = get_object_or_404(Depositor, pk=pk)
        depositor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AccountsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AccountsSerializer

    @swagger_auto_schema(responses={200: AccountsSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        accounts= Accounts.objects.all()
        serializer = AccountsSerializer( accounts, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=AccountsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = AccountsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AccountsSerializer

    @swagger_auto_schema(responses={200: AccountsSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        accounts = get_object_or_404(Accounts, pk=pk)
        serializer = AccountsSerializer(accounts)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AccountsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        accounts= get_object_or_404(Accounts, pk=pk)
        serializer = AccountsSerializer(accounts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        accounts = get_object_or_404(Accounts, pk=pk)
        accounts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TransactionsView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TransactionsSerializer

    @swagger_auto_schema(responses={200: TransactionsSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        transactions= Transactions.objects.all()
        serializer = TransactionsSerializer( transactions, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=TransactionsSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = TransactionsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionsChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TransactionsSerializer

    @swagger_auto_schema(responses={200: TransactionsSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        transactions = get_object_or_404(Transactions, pk=pk)
        serializer = TransactionsSerializer(transactions)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TransactionsSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        transactions= get_object_or_404(Transactions, pk=pk)
        serializer = TransactionsSerializer(transactions, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        transactions = get_object_or_404(Transactions, pk=pk)
        transactions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class Ac_TransferView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Ac_TransferSerializer

    @swagger_auto_schema(responses={200: Ac_TransferSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        ac_transfer= Ac_Transfer.objects.all()
        serializer = Ac_TransferSerializer( ac_transfer, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=Ac_TransferSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = Ac_TransferSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class Ac_TransferChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Ac_TransferSerializer

    @swagger_auto_schema(responses={200: Ac_TransferSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        ac_transfer = get_object_or_404(Ac_Transfer, pk=pk)
        serializer = Ac_TransferSerializer(ac_transfer)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=Ac_TransferSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        ac_transfer= get_object_or_404(Ac_Transfer, pk=pk)
        serializer = Ac_TransferSerializer(ac_transfer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        ac_transfer = get_object_or_404(Ac_Transfer, pk=pk)
        ac_transfer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class Contribution_RefundView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Contribution_RefundSerializer

    @swagger_auto_schema(responses={200: Contribution_RefundSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        contribution_refund= Contribution_Refund.objects.all()
        serializer = Contribution_RefundSerializer( contribution_refund, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=Contribution_RefundSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = Contribution_RefundSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class Contribution_RefundChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Contribution_RefundSerializer

    @swagger_auto_schema(responses={200: Contribution_RefundSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        contribution_refund = get_object_or_404(Contribution_Refund, pk=pk)
        serializer = Contribution_RefundSerializer(contribution_refund)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=Contribution_RefundSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        contribution_refund= get_object_or_404(Ac_Transfer, pk=pk)
        serializer = Contribution_RefundSerializer(contribution_refund, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        contribution_refund = get_object_or_404(Contribution_Refund, pk=pk)
        contribution_refund.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GL_ENTRIES_RECONView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GL_ENTRIES_RECONSerializer

    @swagger_auto_schema(responses={200: GL_ENTRIES_RECONSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        gl_entries_recon= GL_ENTRIES_RECON.objects.all()
        serializer = GL_ENTRIES_RECONSerializer(gl_entries_recon, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=GL_ENTRIES_RECONSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = GL_ENTRIES_RECONSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class GL_ENTRIES_RECONChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GL_ENTRIES_RECONSerializer

    @swagger_auto_schema(responses={200: GL_ENTRIES_RECONSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        gl_entries_recon = get_object_or_404(GL_ENTRIES_RECON, pk=pk)
        serializer = GL_ENTRIES_RECONSerializer(gl_entries_recon)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=GL_ENTRIES_RECONSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        gl_entries_recon= get_object_or_404(Ac_Transfer, pk=pk)
        serializer = GL_ENTRIES_RECONSerializer(gl_entries_recon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        gl_entries_recon = get_object_or_404(GL_ENTRIES_RECON, pk=pk)
        gl_entries_recon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class InvoiceView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = InvoiceSerializer

    @swagger_auto_schema(responses={200: InvoiceSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        invoice= Invoice.objects.all()
        serializer = InvoiceSerializer(invoice, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=InvoiceSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = InvoiceSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = InvoiceSerializer

    @swagger_auto_schema(responses={200: InvoiceSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        invoice = get_object_or_404(Invoice, pk=pk)
        serializer = InvoiceSerializer(invoice)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=InvoiceSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        invoice= get_object_or_404(Ac_Transfer, pk=pk)
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        invoice = get_object_or_404(Invoice, pk=pk)
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SecuritiesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SecuritiesSerializer

    @swagger_auto_schema(responses={200: SecuritiesSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        securities= Securities.objects.all()
        serializer = SecuritiesSerializer(securities, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=SecuritiesSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = SecuritiesSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SecuritiesChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SecuritiesSerializer

    @swagger_auto_schema(responses={200: SecuritiesSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        securities = get_object_or_404(Securities, pk=pk)
        serializer = SecuritiesSerializer(securities)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SecuritiesSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        securities= get_object_or_404(Securities, pk=pk)
        serializer = SecuritiesSerializer(securities, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        securities = get_object_or_404(Securities, pk=pk)
        securities.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssetView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AssetSerializer

    @swagger_auto_schema(responses={200: AssetSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        asset= Asset.objects.all()
        serializer = AssetSerializer(asset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=AssetSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = AssetSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class AssetChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AssetSerializer

    @swagger_auto_schema(responses={200: AssetSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        asset = get_object_or_404(Asset, pk=pk)
        serializer = AssetSerializer(asset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AssetSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        asset= get_object_or_404(Asset, pk=pk)
        serializer = AssetSerializer(asset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        asset = get_object_or_404(Asset, pk=pk)
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SecurityPurchaseView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SecurityPurchaseSerializer

    @swagger_auto_schema(responses={200: SecurityPurchaseSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        securityPurchase= SecurityPurchase.objects.all()
        serializer = SecurityPurchaseSerializer(securityPurchase, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=SecurityPurchaseSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = SecurityPurchaseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SecurityPurchaseChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SecurityPurchaseSerializer

    @swagger_auto_schema(responses={200: SecurityPurchaseSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        securityPurchase = get_object_or_404(SecurityPurchase, pk=pk)
        serializer = SecurityPurchaseSerializer(securityPurchase)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SecurityPurchaseSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        securityPurchase= get_object_or_404(SecurityPurchase, pk=pk)
        serializer = SecurityPurchaseSerializer(securityPurchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        securityPurchase = get_object_or_404(SecurityPurchase, pk=pk)
        securityPurchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SecuritySalesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SecuritySalesSerializer

    @swagger_auto_schema(responses={200: SecuritySalesSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        security_sales= SecuritySales.objects.all()
        serializer = SecuritySalesSerializer(security_sales, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=SecuritySalesSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = SecuritySalesSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SecuritySalesChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SecuritySalesSerializer

    @swagger_auto_schema(responses={200: SecuritySalesSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        security_sales = get_object_or_404(SecuritySales, pk=pk)
        serializer =SecuritySalesSerializer(security_sales)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SecuritySalesSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        security_sales= get_object_or_404(SecuritySales, pk=pk)
        serializer = SecuritySalesSerializer(security_sales, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        security_sales = get_object_or_404(SecuritySales, pk=pk)
        security_sales.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class Upload_Contribution_PaymentView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Upload_Contribution_PaymentSerializer

    @swagger_auto_schema(responses={200: Upload_Contribution_PaymentSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        upload_contribution_payment= Upload_Contribution_Payment.objects.all()
        serializer = Upload_Contribution_PaymentSerializer(upload_contribution_payment, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=Upload_Contribution_PaymentSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = Upload_Contribution_PaymentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class Upload_Contribution_PaymentChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Upload_Contribution_PaymentSerializer

    @swagger_auto_schema(responses={200: Upload_Contribution_PaymentSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        upload_contribution_payment = get_object_or_404(Upload_Contribution_Payment, pk=pk)
        serializer =Upload_Contribution_PaymentSerializer(upload_contribution_payment)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=Upload_Contribution_PaymentSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        upload_contribution_payment= get_object_or_404(Upload_Contribution_Payment, pk=pk)
        serializer = Upload_Contribution_PaymentSerializer(upload_contribution_payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        upload_contribution_payment = get_object_or_404(Upload_Contribution_Payment, pk=pk)
        upload_contribution_payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class WalletWithdrawalView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = WalletWithdrawalSerializer

    @swagger_auto_schema(responses={200: WalletWithdrawalSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        wallet_withdrawal= WalletWithdrawal.objects.all()
        serializer = WalletWithdrawalSerializer(wallet_withdrawal, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=WalletWithdrawalSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = WalletWithdrawalSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class WalletWithdrawalChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = WalletWithdrawalSerializer

    @swagger_auto_schema(responses={200: WalletWithdrawalSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        wallet_withdrawal = get_object_or_404(WalletWithdrawal, pk=pk)
        serializer =WalletWithdrawalSerializer(wallet_withdrawal)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=WalletWithdrawalSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        wallet_withdrawal= get_object_or_404(WalletWithdrawal, pk=pk)
        serializer = WalletWithdrawalSerializer(wallet_withdrawal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        wallet_withdrawal = get_object_or_404(WalletWithdrawal, pk=pk)
        wallet_withdrawal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class WithdrawalRequestView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = WithdrawalRequestSerializer

    @swagger_auto_schema(responses={200: WithdrawalRequestSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        withdrwal_request= WithdrawalRequest.objects.all()
        serializer = WithdrawalRequestSerializer(withdrwal_request, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=WithdrawalRequestSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = WithdrawalRequestSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class WithdrawalRequestChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = WithdrawalRequestSerializer

    @swagger_auto_schema(responses={200: WithdrawalRequestSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        withdrwal_request = get_object_or_404(WithdrawalRequest, pk=pk)
        serializer =WithdrawalRequestSerializer(withdrwal_request)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=WithdrawalRequestSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        withdrwal_request= get_object_or_404(WithdrawalRequest, pk=pk)
        serializer = WithdrawalRequestSerializer(withdrwal_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        withdrwal_request = get_object_or_404(WithdrawalRequest, pk=pk)
        withdrwal_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WalletWithdrawalView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = WalletWithdrawalSerializer

    @swagger_auto_schema(responses={200: WalletWithdrawalSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        withdrwal_request= WalletWithdrawal.objects.all()
        serializer = WalletWithdrawalSerializer(withdrwal_request, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=WalletWithdrawalSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = WalletWithdrawalSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class WalletWithdrawalChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = WalletWithdrawalSerializer

    @swagger_auto_schema(responses={200: WalletWithdrawalSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        withdrwal_request = get_object_or_404(WalletWithdrawal, pk=pk)
        serializer =WalletWithdrawalSerializer(withdrwal_request)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=WalletWithdrawalSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        withdrwal_request= get_object_or_404(WalletWithdrawal, pk=pk)
        serializer = WalletWithdrawalSerializer(withdrwal_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        withdrwal_request = get_object_or_404(WalletWithdrawal, pk=pk)
        withdrwal_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)