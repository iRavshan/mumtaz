from datetime import datetime
from django.shortcuts import get_object_or_404
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
    
    @action(detail=False, methods=['get'], url_path='check-existence')
    def check_existence(self, request):
        phone_number = request.query_params.get('phone_number')
        
        if not phone_number:
            return Response(
                {"error": "Phone number is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        exists = Customer.objects.filter(phone_number=phone_number).exists()
        if exists:
            return Response(
                {"message": "Customer exists in the database."},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "Customer does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
            
    
    @action(detail=False, methods=['get'], url_path='check-telegram')
    def check_telegram(self, request):
        telegram_id = request.query_params.get('telegram_id')
        if not telegram_id:
            return Response({"error": "Telegram ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            customer = Customer.objects.get(telegram_id=telegram_id)
            return Response(
                {
                    "message": "Customer is registered on Telegram.",
                    "customer": {
                        "id": customer.id,
                        "first_name": customer.first_name,
                        "phone_number": customer.phone_number,
                        "address": customer.address,
                    }
                },
                status=status.HTTP_200_OK
            )
        except Customer.DoesNotExist:
            return Response({"message": "Customer is not registered on Telegram."}, status=status.HTTP_404_NOT_FOUND)
    
    
    @action(detail=False, methods=['get'], url_path='active-orders')
    def get_active_orders(self, request, pk=None):
        customer = get_object_or_404(Customer, pk=pk)
        undelivered_orders = Order.objects.filter(customer=customer, status__in=['new', 'received', 'delivering'])
        
        if not undelivered_orders.exists():
            return Response({'detail': 'No undelivered orders found for this customer.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = OrderSerializer(undelivered_orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

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