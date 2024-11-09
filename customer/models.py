from uuid import uuid4
from django.db import models
from common.models import BaseModel
from common.generators import customer_key_generator

class Customer(BaseModel):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)
    key = models.CharField(max_length=10, unique=True, auto_created=True, null=False, editable=False, default=customer_key_generator)
    first_name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=12, null=False, unique=True)
    address = models.CharField(max_length=200, null=False)
    geo_location = models.URLField(null=True)
    
    def __str__(self):
        return f'{self.key} - {self.first_name} - {self.phone_number}'
    
    class Meta:
        ordering = ['-created_at']