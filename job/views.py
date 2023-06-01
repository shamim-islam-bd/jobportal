from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework import status 
from django.db.models import Avg, Count, Min, Sum, Max
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated

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
         
        # before post user must be authenticated
        permission_classes = [IsAuthenticated]
        
        # request.data['user'] = request.user
        
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
        
        # before put user must be authenticated
        permission_classes = [IsAuthenticated]
        
        job = get_object_or_404(Job, pk=pk)
        
        # check if user is the owner of the job then he can only update this job.
        if job.user != request.user:
            return Response({"message": "You are not authorized to update this job."}, status=status.HTTP_401_UNAUTHORIZED)
        
        
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
        
        # before delete user must be authenticated
        permission_classes = [IsAuthenticated]
        
        job = get_object_or_404(Job, pk=pk)
        
        # check if user is the owner of the job then he can only delete this job.
        if job.user != request.user:
            return Response({"message": "You are not authorized to delete this job."}, status=status.HTTP_401_UNAUTHORIZED)

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



class ApplyToJob(APIView): 
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        
        # check if resume is uploaded or not
        if not request.user.userprofile.resume:
            return Response({"message": "Please upload your resume first."}, status=status.HTTP_401_UNAUTHORIZED)
        
        # check if user already applied to this job then he can not apply to this job again.
        if job.candidateapplied_set.filter(user=request.user).exists():
            return Response({"message": "You already applied to this job."}, status=status.HTTP_401_UNAUTHORIZED)
        
        # check if job last date is expired then user can not apply to this job.
        if job.lastDate < timezone.now():
            return Response({"message": "Job last date is expired."}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        job.candidateapplied_set.create(user=request.user)
        return Response({"message": "You applied to this job successfully."}, status=status.HTTP_200_OK)