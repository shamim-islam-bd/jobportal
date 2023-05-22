
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status 
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Job


from .serializers import JobSerializers

# Create your views here.

class Jobs(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializers(jobs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        job = Job.objects.create(**data)
        
        serializer = JobSerializers(job, many=False)
        return Response(serializer.data)
    
    
    
class JobDetail(APIView):
    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        
        serializer = JobSerializers(job, many=False)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        
        job.title = request.data['title']
        job.description = request.data['description']
        job.email = request.data['email']
        job.address = request.data['address']
        job.jobType = request.data['job']
        job.education = request.data['education']
        job.industry = request.data['industry']
        job.experience = request.data['experience']
        job.salary = request.data['salary']
        job.positons = request.data['positons']
        job.company = request.data['company']
        
        job.save()
        serializer = JobSerializers(job, many=False)
        
        return Response(serializer.data)
    
    
    def delete(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)