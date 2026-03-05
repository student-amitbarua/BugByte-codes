from django.http import JsonResponse
from api.serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer
from api.models import Product, Order, OrderItem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.db.models import Max
from rest_framework import generics



# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return JsonResponse ({
#         'data' : serializer.data
#     }) #ei function use kora hoise data k json formate a show korar jonno 



# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data) # ei function use kora hoise data api format e show koranor jonno


# use ?format=jsaon its atumatecly convert api into json format



class ProductLlistAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(stock__gt=0)  # 0 theke boro stock gula dekhabe
    queryset = Product.objects.exclude(stock__gt=0) 
    serializer_class = ProductSerializer


# @api_view(['GET'])
# def product_Detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product)   #we don't need all data thats the reason i remove the many = true
#     return Response(serializer.data)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer



class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

# @api_view(['GET'])
# def order_list(request):
#     orders = Order.objects.prefetch_related('items__product')
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'Products' : products,
        'count': len(products),
        'max_price': products.aggregate(max_price= Max('price')) ['max_price']
    })
    return Response(serializer.data)


