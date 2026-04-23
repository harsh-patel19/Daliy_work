from rest_framework import serializers
from myapp.models import *

class ProductSeraializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"