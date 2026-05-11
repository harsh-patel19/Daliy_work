from rest_framework import serializers 
from myapp.models import *

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields ="__all__"

        