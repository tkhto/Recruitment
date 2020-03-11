from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path("province/", views.ProvinceAPIView.as_view()),
    path("jobs/", views.JobsAPIView.as_view()),
    path("position/", views.PositionListAPIView.as_view()),
    path("company/", views.CompanyListAPIView.as_view()),
    re_path("position/(?P<pk>\d+)/$", views.PositionRetrieveAPIView.as_view()),
    re_path("company/(?P<companyId>\d+)/$", views.CompanyRetrieveAPIView.as_view()),
    path("PosFilterRequire/", views.PosFilterRequire),
    path("ComFilterRequire/", views.ComFilterRequire),
]
