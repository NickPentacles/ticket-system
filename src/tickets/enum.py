from django.db import models


class Statuses(models.TextChoices):
    HOLD = '1', 'HOLDING'
    SUBMIT = '2', 'SUBMITED'
    COMPLETE = '3', 'COMPLETED'
    FAIL = '4', 'FAILED'
