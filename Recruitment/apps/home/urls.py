from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path("province/", views.ProvinceAPIView.as_view()),
    path("jobs/", views.JobsAPIView.as_view()),
]
