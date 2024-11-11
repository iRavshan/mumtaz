from datetime import datetime
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from courier.models import Courier
from courier.serializers import CourierSerializer
from customer.models import Customer
from customer.serializers import CustomerSerializer
from order.models import Order
from order.serializers import OrderSerializer


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
    
    @action(detail=False, methods=['post'], url_path='login', permission_classes=[AllowAny])
    def login(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        if not phone_number or not password:
            return Response({'detail': 'Phone number and password are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        courier = Courier.objects.filter(phone_number=phone_number, password=password).first()

        if courier:
            return Response({'detail': 'Login successful', 'courier_id': courier.id},
                            status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid phone number or password.'},
                            status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(detail=True, methods=['get'], url_path='new-orders')
    def new_orders(self, request, pk=None):
        courier = self.get_object()
        new_orders = Order.objects.filter(courier=courier, status='received')
        serializer = OrderSerializer(new_orders, many=True)
        return Response(serializer.data)
        
    
    
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    @action(detail=True, methods=['post'], url_path='mark-as-delivered', permission_classes=[AllowAny])
    def mark_as_delivered(self, request, pk=None):
        order = self.get_object()
        order.status = 'delivered'
        order.delivered_at = datetime.now()
        order.save()
        return Response({'status': 'Order marked as delivered'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='filter-by-status')
    def filter_by_status(self, request):
        status_param = request.query_params.get('status')
        if not status_param:
            return Response({'error': 'Status parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        orders = self.queryset.filter(status=status_param)
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)