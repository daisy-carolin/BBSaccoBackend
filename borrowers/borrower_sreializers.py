from rest_framework import serializers, fields

from .borrowers import *
from .branches import *
from .add_borrowers import *

class Borrowers1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowers1
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model =Branch
        fields = "__all__"


class AddUserInBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddUserInBranch
        fields = "__all__"


class AddBorrowersGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddBorrowersGroup
        fields = "__all__"