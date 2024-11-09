from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)

    def __str__(self):
        return self.username