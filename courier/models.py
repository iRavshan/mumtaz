from uuid import uuid4
from django.db import models
from common.models import BaseModel
from common.generators import courier_key_generator, courier_password_generator

class Courier(BaseModel):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)
    key = models.CharField(max_length=10, unique=True, auto_created=True, null=False, editable=False, default=courier_key_generator)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    car_number = models.CharField(max_length=8, null=False)
    payload = models.PositiveIntegerField(default=0, null=False)
    phone_number = models.CharField(max_length=12, null=False, unique=True)
    password = models.CharField(max_length=8, null=False, auto_created=True, default=courier_password_generator)
    is_banned = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.car_number = self.car_number.upper()
        self.first_name = self.first_name.lower().capitalize()
        self.last_name = self.last_name.lower().capitalize()
        super(Courier, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name']