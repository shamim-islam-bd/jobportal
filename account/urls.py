from django.urls import path
from .views import SignUp, currentUser, UserView

urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),
    path('update/', UserView.as_view(), name="userView"),
    path('me/', currentUser, name="currentuser"),
]
