from uuid import uuid4
from django.db import models
from common.models import BaseModel
from common.generators import courier_key_generator

class Courier(BaseModel):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)
    key = models.CharField(max_length=10, unique=True, auto_created=True, null=False, editable=False, default=courier_key_generator)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    photo_uri = models.URLField(null=True, blank=True)
    payload = models.PositiveIntegerField(default=0, null=False)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name']