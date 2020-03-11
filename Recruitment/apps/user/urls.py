from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path("geetest/", views.GeetestCapchaAPIView.as_view()),
    path("", views.AccountAPIView.as_view()),
    re_path("sms/(?P<mobile>1[3-9]\d{9})/", views.SMSAPIView.as_view()),
    path("avatar/", views.avatar_upload),
    re_path("profile/(?P<pk>\d+)/$", views.AccountViewset.as_view({'get': 'retrieve', 'post': 'partial_update'})),

    path("news/", views.NewsViewset.as_view({'get': 'list', 'post': 'create'})),
    re_path("news_del/(?P<pk>\d+)/", views.NewsViewset.as_view({'delete': 'destroy'})),

    path("article/", views.ArticleViewset.as_view({'get': 'list', 'post': 'create'})),
    re_path("article_del/(?P<pk>\d+)/", views.ArticleViewset.as_view({'delete': 'destroy'})),
    re_path("article/(?P<pk>\d+)/", views.ArticleRetrieve.as_view({'get': 'retrieve', 'post': 'partial_update'})),
    re_path("articlecomment/(?P<aid>\d+)", views.ArticleCommentsViewset.as_view({'get': 'list', 'post': 'create'})),

    path("resume/", views.ResumeViewset.as_view({'get': 'list', 'post': 'create'})),
    re_path("resume_del/(?P<pk>\d+)/", views.ResumeViewset.as_view({'delete': 'destroy'})),
    re_path("resume/(?P<pk>\d+)/", views.ResumeRetrieve.as_view({'get': 'retrieve', 'post': 'partial_update'}))
]