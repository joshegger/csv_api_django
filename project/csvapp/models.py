from django.db import models
from datetime import timedelta

# here we set id as the primary key and define the remaining fields
# Timestamp - Date Time
# Temperature - Float
# Duration - Duration Field

class Metrics(models.Model):

    id = models.IntegerField(primary_key=True, unique=True)
    timestamp = models.DateTimeField(blank=False)
    temperature = models.FloatField(blank=False)
    duration = models.CharField(max_length=100)

    class Meta:
        def __str__(self):
            return self.id

        db_table = 'Metrics'

class Logs(models.Model):
    timestamp = models.CharField(max_length=1024)
    pageURL = models.CharField(max_length=1024)

    class Meta:

        db_table = "Logs"
