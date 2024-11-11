from rest_framework import serializers
from courier.models import Courier


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ['id', 'key', 'first_name', 'last_name', 'photo_uri', 'payload', 'phone_number', 'password']
        read_only_fields = ['id', 'key', 'password']