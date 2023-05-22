
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status 
from django.db.models import Avg, Count, Min, Sum, Max
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Job
from .serializers import JobSerializers
from .filters import JobsFilter

# Create your views here.

class Jobs(APIView):
    def get(self, request):
        
        # filtering all jobs by jobType, education, industry, experience, min_salary, max_salary, keyword, location
        filterset = JobsFilter(request.GET, queryset=Job.objects.all().order_by('id'))
        
        count = filterset.qs.count() # count total number of jobs
        
        # pagination applied
        perPage = 2
        paginator = PageNumberPagination()
        paginator.page_size = perPage
        result_page = paginator.paginate_queryset(filterset.qs, request)
        
        serializer = JobSerializers(result_page, many=True)
        return Response({
            'count': count,
            'resPerPage': perPage,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'jobs': serializer.data
        })
    
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
        return Response( {"Job deleted "}, status=status.HTTP_204_NO_CONTENT)
    
    
    
class JobStats(APIView):
    def get(self, request, topic):

        args = { 'title__icontains': topic }
        jobs = Job.objects.filter(**args)

        if len(jobs) == 0:
          return Response({"message": "No starts found for {topic}".format(topic=topic)})
        
        start = jobs.aggregate(
            total__jobs = Count('title'),
            avg__position = Avg('positon'),
            Avg__salary = Avg('salary'),
            min__salary = Min('salary'),
            max__salary = Max('salary'),
        )
        
        return Response(start)
