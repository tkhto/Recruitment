from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path("geetest/", views.GeetestCapchaAPIView.as_view()),
    path("", views.AccountAPIView.as_view()),
    re_path("sms/", views.SMSAPIView.as_view()),
    path("avatar/", views.avatar_upload),
    re_path("profile/(?P<pk>\d+)/$", views.AccountViewset.as_view({'get': 'retrieve', 'post': 'partial_update'})),
    path("change_user_type/", views.change_user_type),
    path("user_auth/", views.user_auth),

    path("news/", views.NewsViewset.as_view({'get': 'list', 'post': 'create'})),
    re_path("news_del/(?P<pk>\d+)/", views.NewsViewset.as_view({'delete': 'destroy'})),

    path("article/", views.ArticleViewset.as_view({'get': 'list', 'post': 'create'})),
    re_path("article_del/(?P<pk>\d+)/", views.ArticleViewset.as_view({'delete': 'destroy'})),
    re_path("article/(?P<pk>\d+)/", views.ArticleRetrieve.as_view({'get': 'retrieve', 'post': 'partial_update'})),
    re_path("articlecomment/(?P<aid>\d+)", views.ArticleCommentsViewset.as_view({'get': 'list', 'post': 'create'})),

    path("resume/", views.ResumeViewset.as_view({'get': 'list', 'post': 'create'})),
    re_path("resume_del/(?P<pk>\d+)/", views.ResumeViewset.as_view({'delete': 'destroy'})),
    re_path("resume/(?P<pk>\d+)/", views.ResumeRetrieve.as_view({'get': 'retrieve', 'post': 'partial_update'})),
    path("delivery/", views.DeliveryViewset.as_view({'post': 'create'})),
    re_path("delivery/user/(?P<user>\d+)/", views.delivery_record),
    re_path("received/user/(?P<user>\d+)/", views.received_record),
    re_path("received/change/(?P<pk>\d+)/", views.received_change),
    re_path("delivery/delete/(?P<pk>\d+)/", views.delivery_delete),
    re_path("delivery/(?P<pk>\d+)/", views.DeliveryViewset.as_view({'get': 'retrieve'})),
]