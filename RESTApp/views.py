from django.shortcuts import render
from RESTApp.models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
@api_view(['GET','POST'])
def ProductList(request):
    if request.method=='GET':
        obj=Product.objects.all()
        serializer=ProductSerializer(obj,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def ProductDetail(request,pk):
    try:
        obj=Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=ProductSerializer(obj)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=ProductSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        obj.delete()
        return Response(status=status.HTTP_200_OK)





#
