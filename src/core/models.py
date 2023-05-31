from django.db import models
from django.contrib.auth import get_user_model

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


class CreatorRequestExecutor(models.Model):

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

    class Statuses(models.TextChoices):
        HLD = '1', 'HOLDING'
        SUB = '2', 'SUBMITED'
        COM = '3', 'COMPLETED'
        FAI = '4', 'FAILED'

    status = models.CharField(
        max_length=3,
        choices=Statuses.choices,
        default=Statuses.HLD
        )
