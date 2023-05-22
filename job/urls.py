from django.urls import path
from .views import Jobs, JobDetail

urlpatterns = [
    path('jobs/', Jobs, name="jobs"),
    path('jobs/<str:pk>/', JobDetail, name="job-detail"),
]
