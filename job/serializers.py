from rest_framework import serializers
from .models import Job

# Create your models here.
class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        
        
        