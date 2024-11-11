from rest_framework import serializers
from courier.models import Courier
from customer.models import Customer
from order.models import Order
from user.models import CustomUser


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    courier = serializers.PrimaryKeyRelatedField(queryset=Courier.objects.all(), required=False)
    received_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False) 

    class Meta:
        model = Order
        fields = [
            'id',
            'key',
            'customer',
            'replacement_bottles',
            'new_bottles',
            'destination',
            'geo_location',
            'received_by',
            'received_at',
            'courier',
            'delivered_at',
            'asap_delivery',
            'preferred_delivery_datetime',
            'status',
        ]
        read_only_fields = ['id', 'key', 'received_by', 'status']