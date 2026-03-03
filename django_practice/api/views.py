from django.http import JsonResponse
from api.serializers import ProductSerializer
from api.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return JsonResponse ({
#         'data' : serializer.data
#     }) #ei function use kora hoise data k json formate a show korar jonno 



@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data) # ei function use kora hoise data api format e show koranor jonno


# use ?format=jsaon its atumatecly convert api into json format


@api_view(['GET'])
def product_Detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)   #we don't need all data thats the reason i remove the many = true
    return Response(serializer.data)