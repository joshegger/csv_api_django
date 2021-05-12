from rest_framework import serializers
from .models import Metrics, Logs

class DataSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    timestamp = serializers.DateTimeField(required=False)
    temperature = serializers.FloatField(required=False)
    duration = serializers.CharField(required=False) 

    class Meta:
        model = Metrics
        fields = ('id', 'timestamp', 'temperature', 'duration')

class LogSerializer(serializers.ModelSerializer):
    timestamp = serializers.CharField(required=False)
    pageURL = serializers.CharField(required=False)

    class Meta:
        model = Logs
        fields = ('user', 'pageURL')