from rest_framework import serializers
from .models import Job, CandidateApplied

# Create your models here.
class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        
        
        
class CandidedAppliedSerializers(serializers.ModelSerializer):
    
    job = JobSerializers()
    
    class Meta:
        model = CandidateApplied
        fields = '__all__'
        
        
        