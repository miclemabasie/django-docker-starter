from django.urls import path
from .controllers import GetProfileAPIView, profile_update, update_user_role

app_name = "users_api"

urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="my_profile"),
    path("update/", profile_update, name="update_profile"),
    path("update-role/", update_user_role, name="update_user_role"),
]
