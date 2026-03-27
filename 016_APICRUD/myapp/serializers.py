from rest_framework import serializers
from myapp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coruse
        fields = "__all__"

