from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path("geetest/", views.GeetestCapchaAPIView.as_view()),
    path("", views.AccountAPIView.as_view()),
    re_path("sms/(?P<mobile>1[3-9]\d{9})/", views.SMSAPIView.as_view()),
]