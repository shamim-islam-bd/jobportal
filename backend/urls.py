
from django.contrib import admin 
from django.urls import path , include 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('job.urls')),
    path('api/', include('account.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    
]

urlpatterns += staticfiles_urlpatterns()

handler500 =  'utils.error_views.handler500'
error_404 =  'utils.error_views.error_404'