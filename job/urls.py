from django.urls import path
from .views import Jobs, JobDetail, JobStats, ApplyToJob, CurrentUserAppliedJob

urlpatterns = [
    path('jobs/', Jobs.as_view(), name="jobs"),
    path('jobs/<str:pk>/', JobDetail.as_view(), name="job-detail"),
    path('stats/<str:topic>/', JobStats.as_view(), name="job-stats"),
    
    path('jobs/<str:pk>/apply/', ApplyToJob.as_view(), name='applyTojob'),
    path('me/jobs/applied/', CurrentUserAppliedJob.as_view(), name='current_user_applied_Job'),
]
