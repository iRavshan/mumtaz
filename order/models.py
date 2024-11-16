from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from common.models import BaseModel
from common.generators import order_key_generator
from customer.models import Customer
from courier.models import Courier
from user.models import CustomUser


class Order(BaseModel):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)
    key = models.CharField(max_length=10, unique=True, auto_created=True, null=False, editable=False, default=order_key_generator)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    replacement_bottles = models.PositiveSmallIntegerField(default=0, null=False, validators=[MinValueValidator(0)])
    new_bottles = models.PositiveSmallIntegerField(default=0, null=False, validators=[MinValueValidator(0)])

    received_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    received_at = models.DateTimeField(null=True, blank=True)
    
    courier = models.ForeignKey(Courier, null=True, on_delete=models.SET_NULL, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    
    asap_delivery = models.BooleanField(default=True, null=False)
    preferred_delivery_datetime = models.DateTimeField(null=True, blank=True)
    
    ORDER_STATUS_CHOICES = [
        ('new', 'Yangi'),
        ('received', 'Qabul qilingan'),
        ('delivering', 'Yetkazilmoqda'),
        ('delivered', 'Yetkazilgan'),
        ('cancelled', 'Bekor qilingan'),
    ]
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='new')
    
    
    def clean(self):
        super().clean()
        if not self.replacement_bottles and not self.new_bottles:
            raise ValidationError("Sotib olinayotgan suvlar sonini kiritishingiz zarur.")
    
    
    def save(self, *args, **kwargs):
        self.clean()
        if self.asap_delivery:
            self.preferred_delivery_datetime = None
        else:
            if not self.preferred_delivery_datetime:
                raise ValueError("Tezkor bo'lmagan yetkazish turi uchun yetkazish vaqti va sanasini kiritish lozim.")
        super(Order, self).save(*args, **kwargs)
        
        
    def __str__(self):
        return f"Order {self.key} for {self.customer}"
    
    class Meta:
        ordering = ['-created_at']