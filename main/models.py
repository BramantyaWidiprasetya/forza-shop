from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()  # Remove max_length, as it's not needed for IntegerField
    description = models.TextField()  # Add parentheses to correctly define the field
