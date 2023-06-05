from django.urls import path
from .views import Jobs, JobDetail, JobStats, ApplyToJob, CurrentUserAppliedJob, isAppliedToJob, CurrentUserJobs, CandidatesApplied

urlpatterns = [
    path('jobs/', Jobs.as_view(), name="jobs"),
    path('me/jobs/', CurrentUserJobs.as_view(), name='current_user_Jobs'),
    path('jobs/<str:pk>/', JobDetail.as_view(), name="job-detail"),
    path('stats/<str:topic>/', JobStats.as_view(), name="job-stats"),
    
    path('jobs/<str:pk>/apply/', ApplyToJob.as_view(), name='applyTojob'),
    path('me/jobs/applied/', CurrentUserAppliedJob.as_view(), name='current_user_applied_Job'),
    
    path('jobs/<str:pk>/check/', isAppliedToJob.as_view(), name="isAppilied_to_job"),
    
    path('jobs/<str:pk>/candidates/', CandidatesApplied.as_view(), name='job-candidates')
]
