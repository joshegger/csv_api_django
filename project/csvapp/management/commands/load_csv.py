from csv import DictReader
from django.core.management import BaseCommand
from django.db import models
from csvapp.models import Metrics
import os, csv
from django.conf import settings
import datetime
from django.apps import apps


from django.utils import timezone
datetime.datetime.now(tz=timezone.utc)

class Command(BaseCommand):
    # Show when user types help
    help = "Loads data from task_data.csv"

    def handle(self, *args, **options):

        # Show if the db already seeded with data
       # if Metrics.objects.exists():
          #  print('data already loaded...exiting.')
           # return

        # Show before loading the data into the database
        print("Loading metrics data")

        # Load data into database
        #for row in DictReader(open('./task_data.csv')):
        #    MetricsDB = Metrics(id=row['id'], timestamp=row['timestamp'], temperature=row['temperature'], duration=row['duration'])
          #  MetricsDB.save()

        with open(os.path.join(settings.BASE_DIR, 'task_data.csv')) as csvfile:
            #Metrics = apps.get_model('csvapp', 'Metrics')
            for row in csv.DictReader(csvfile):
                Metrics.objects.create(**row)
                m = Metrics(category='log_time', length=19, aphorism='i love life')
                m.save()


   
