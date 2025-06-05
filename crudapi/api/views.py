from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer

# Telling DRF what metod we are using in this API view function.
@api_view(["GET", "POST"])
def product_list(request):

    if request.method == "GET":

        # Get list of all products 
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True) # many - all data will be serialized

        return Response(serializer.data)
    
    if request.method == "POST":

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
