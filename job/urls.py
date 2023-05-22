from django.urls import path
from .views import Jobs, JobDetail, JobStats

urlpatterns = [
    path('jobs/', Jobs.as_view(), name="jobs"),
    path('jobs/<str:pk>/', JobDetail.as_view(), name="job-detail"),
    path('stats/<str:topic>', JobStats.as_view(), name="job-stats"),
]
