from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import jsonfield
from django.conf import settings
from .validators import validate_patnof
from django import forms


class Patent(models.Model):
    patnof = models.IntegerField(null=True, validators=[validate_patnof])
    claim_list = models.JSONField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username


   