from django.urls import path
from .views import SignUp, currentUser, UserView

urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),
    path('update/', UserView.as_view(), name="userView"),
    path('me/', currentUser, name="currentuser"),
    # path('update/', profileUpdate.as_view(actions={'get': 'list', 'post': 'create', 'put': 'update'}), name="upload_resume")
]
