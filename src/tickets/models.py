from django.db import models
from django.contrib.auth import get_user_model
from .enum import Statuses

User = get_user_model()


class Request(models.Model):
    name = models.CharField(
        max_length=150,
        editable=True,
        name='name'
    )
    description = models.CharField(
        max_length=400,
        editable=True,
        name='description'
    )
    create_dt = models.DateField(
        auto_now_add=True,
        name='created'
    )


class Ticket(models.Model):

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='creator'
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, default=None,
        related_name='executor',
        editable=True
    )
    request = models.ForeignKey(
        Request,
        on_delete=models.CASCADE,
        name='request'
    )
    end_dt = models.DateField(
        null=True,
        editable=True,
        default=None,
        name='deadline'
    )

    status = models.CharField(
        max_length=6,
        choices=Statuses.choices,
        default=Statuses.HOLD
    )
