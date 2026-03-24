from django.shortcuts import render
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import *
from api.models import *
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method == "GET":
        return Response("Public can view this data")
    
    elif request.method == "POST":
        return Response("Only authencaticated users can post data")
    
    
    