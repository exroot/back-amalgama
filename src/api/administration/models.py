from django.db import models
from src.api.users.models import User
from src.helpers.models import TrackingModel
from django.db.models.signals import post_save

OPERATION_CREATE = "create"
OPERATION_UPDATE = "edit"
OPERATION_DELETE = "delete"
OPERATION_REPORT = "report"

class Activity(TrackingModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    operation = models.CharField(max_length=255)
    resource = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user) + " " + self.operation + "" + self.resource

