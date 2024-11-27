from rest_framework import serializers
from courier.models import Courier
from customer.models import Customer
from order.models import Order
from user.models import CustomUser


class OrderSerializer(serializers.ModelSerializer):    
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    courier = serializers.PrimaryKeyRelatedField(queryset=Courier.objects.all(), required=False)
    received_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False) 
    customer_details = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id',
            'key',
            'customer',
            'replacement_bottles',
            'new_bottles',
            'received_by',
            'received_at',
            'courier',
            'delivered_at',
            'asap_delivery',
            'preferred_delivery_datetime',
            'status', 
            'customer_details'
        ]
        read_only_fields = ['id', 'key', 'received_by', 'status']
        
    def get_customer_details(self, obj):
        if obj.customer:
            return {
                'address': obj.customer.address,
                'geo_location': obj.customer.geo_location,
                'phone_number': obj.customer.phone_number
            }
        return None