from django.shortcuts import render
from .models import Metrics, Logs
from django.views import View
from rest_framework.generics import ListAPIView
from .serializer import DataSerializer



class MetricsSearchView(ListAPIView):
    serializer_class = DataSerializer
    queryset = Metrics.objects.all()
    

    def get_queryset(self):


        fields = ['id', 'timestamp', 'temperature', 'duration']
        queryset = Metrics.objects.all()

        return queryset

class LogsView(ListAPIView):
    serializer_class = DataSerializer
    queryset = Logs.objects.all()

    def get_queryset(self):


        fields = ['timestamp', 'pageURL']
        queryset = Logs.objects.all()

        return queryset
