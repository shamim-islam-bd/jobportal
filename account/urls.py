from django.urls import path
from .views import SignUp, currentUser, UserView, uploadResume

urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),
    path('update/', UserView.as_view(), name="userView"),
    path('me/', currentUser, name="currentuser"),
    path('upload/', uploadResume.as_view(), name="upload_resume")
]