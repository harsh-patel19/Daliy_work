from rest_framework.serializers import *
from myapp.models import *

class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"