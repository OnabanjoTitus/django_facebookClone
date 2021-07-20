import datetime

from django.db import models


# Create your models here.
class UserInfo(models.Model):
    Last_period_date = models.DateField()
    Cycle_average = models.IntegerField()
    Period_average = models.CharField()
    Start_date = models.DateField()
    end_date = models.DateField()


class LadyCycle(models.Model):
    Period_start_date = UserInfo.Last_period_date + datetime.timedelta(days=float(UserInfo.Cycle_average))

