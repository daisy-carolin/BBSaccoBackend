from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from .borrower_sreializers import AddBorrowersGroupSerializer, AddUserInBranchSerializer, Borrowers1Serializer, BranchSerializer

# Create your views here.

from datetime import datetime
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .borrowers import *
from .branches import *
from .add_borrowers import *

from django.contrib.auth.hashers import make_password

from .borrower_sreializers import *

class BranchView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BranchSerializer

    @swagger_auto_schema(responses={200: BranchSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        branch= Branch.objects.all()
        serializer = BranchSerializer( branch, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=BranchSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = BranchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BranchChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BranchSerializer

    @swagger_auto_schema(responses={200: BranchSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        branch = get_object_or_404(Branch, pk=pk)
        serializer = BranchSerializer(branch)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=BranchSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        branch = get_object_or_404(Branch, pk=pk)
        serializer = BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        branch = get_object_or_404(Branch, pk=pk)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class Borrowers1View(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Borrowers1Serializer

    @swagger_auto_schema(responses={200: Borrowers1Serializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        branch= Borrowers1.objects.all()
        serializer = Borrowers1Serializer( branch, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=Borrowers1Serializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = Borrowers1Serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        

class Borrowers1ChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Borrowers1Serializer

    @swagger_auto_schema(responses={200: Borrowers1Serializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        branch = get_object_or_404(Borrowers1, pk=pk)
        serializer = Borrowers1Serializer(branch)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=Borrowers1Serializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        branch = get_object_or_404(Borrowers1, pk=pk)
        serializer = Borrowers1Serializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        branch = get_object_or_404(Borrowers1, pk=pk)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class BranchView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BranchSerializer

    @swagger_auto_schema(responses={200: BranchSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        branch= Branch.objects.all()
        serializer = BranchSerializer( branch, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=BranchSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = BranchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BranchChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BranchSerializer

    @swagger_auto_schema(responses={200: BranchSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        branch = get_object_or_404(Branch, pk=pk)
        serializer = BranchSerializer(branch)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=BranchSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        branch = get_object_or_404(Branch, pk=pk)
        serializer = BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        branch = get_object_or_404(Borrowers, pk=pk)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class AddUserInBranchView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AddUserInBranchSerializer

    @swagger_auto_schema(responses={200: AddUserInBranchSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        add_user_in_branch= AddUserInBranch.objects.all()
        serializer = AddUserInBranchSerializer( add_user_in_branch, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=AddUserInBranchSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = AddUserInBranchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        

class AddUserInBranchChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AddUserInBranchSerializer

    @swagger_auto_schema(responses={200: AddUserInBranchSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        add_user_in_branch = get_object_or_404(AddUserInBranch, pk=pk)
        serializer = AddUserInBranchSerializer(add_user_in_branch)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AddUserInBranchSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        add_user_in_branch = get_object_or_404(AddUserInBranch, pk=pk)
        serializer = AddUserInBranchSerializer(add_user_in_branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        add_user_in_branch = get_object_or_404(AddUserInBranch, pk=pk)
        add_user_in_branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class AddBorrowersGroupView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AddBorrowersGroupSerializer

    @swagger_auto_schema(responses={200: AddBorrowersGroupSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        add_borrowers_group= AddBorrowersGroup.objects.all()
        serializer = AddBorrowersGroupSerializer( add_borrowers_group, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=AddBorrowersGroupSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = AddBorrowersGroupSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        

class AddBorrowersGroupChangeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AddBorrowersGroupSerializer

    @swagger_auto_schema(responses={200: AddBorrowersGroupSerializer})
    def get(self, request,pk, format=None, *args, **kwargs):
        add_borrowers_group = get_object_or_404(AddBorrowersGroup, pk=pk)
        serializer = AddBorrowersGroupSerializer(add_borrowers_group)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AddBorrowersGroupSerializer)
    def put(self, request, pk, format=None, *args, **kwargs):
        add_borrowers_group = get_object_or_404(AddBorrowersGroup, pk=pk)
        serializer = AddBorrowersGroupSerializer(add_borrowers_group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None, *args, **kwargs):
        add_borrowers_group = get_object_or_404(AddBorrowersGroup, pk=pk)
        add_borrowers_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
