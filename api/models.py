from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class UserProfile(models.Model):
    LOGGED_OUT = 0
    LOGGED_IN = 1
    ACCOUNT_STATUS_CHOCIES = [
        (LOGGED_OUT, 'You are logged out'),
        (LOGGED_IN, 'You are logged in'),
    ]
    name = CharField(max_length=10)
    status = models. IntegerField(choices=ACCOUNT_STATUS_CHOCIES)