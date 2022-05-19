from django.urls import path
from .views import UserApiView

urlpatterns = [
    path("account/", UserApiView.as_view(), name="user")
]
