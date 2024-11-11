from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'key', 'first_name', 'phone_number', 'address', 'geo_location']
        read_only_fields = ['id', 'key']