from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
         
         model = Product
         fields = (
              'description',
              'name',
               'price',
               'stock',

         )

         def validate_price(self, value):
              if value <= 0:
                   
                   raise serializers.ValidationError(
                        "price must be greater than 0"
                   )
              
              return value
         

class OrderItemSerializer(serializers.ModelSerializer):
     
    #  product =ProductSerializer() #fetch kore data er vetor data dey

    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(
         max_digits=10,
         decimal_places=2,
         source='product.price')

    class Meta:
          model = OrderItem
          fields = ('product_name', 'product_price', 'order')



class OrderCreateSerializer(serializers.ModelSerializer):
      class OrderItemCreateSerializer(serializers.ModelSerializer):
           class Meta:
                model = OrderItem
                fields = ('product', 'quantity')

      items = OrderItemCreateSerializer(many=True)

      def create(self, validated_data):
           orderitem_data = validated_data.pop('items')
           order = Order.objects.create(**validated_data)

           for item in orderitem_data:
                OrderItem.objects.create(order=order, **item)

           return order
                                      
      class Meta:
           model = Order
           fields = ( 'order_id',
                    'user', 
                    'status', 
                    'items', 
                    )
           extra_kwargs = {
                'user': {'read_only': True}
           }


class OrderSerializer(serializers.ModelSerializer):
     order_id = serializers.UUIDField(read_only=True) # you just read but don't get any input
     items = OrderItemSerializer(many=True, read_only=True)

     total_price = serializers.SerializerMethodField(method_name='total')

     def total(self, obj):
          order_items = obj.items.all()
          return sum(order_item.item_subtotal for order_item in order_items)

     class Meta:
          model = Order
          fields = ('order_id', 
                    'created_at', 
                    'user', 
                    'status', 
                    'items', 
                    'total_price')

class ProductInfoSerializer(serializers.Serializer):
     # get all product, count of poducts, max price

     Products = ProductSerializer(many=True)
     count = serializers.IntegerField()
     max_price = serializers.FloatField()