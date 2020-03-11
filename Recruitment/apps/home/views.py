from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from . import models
from . import serializers
from . import paginations
from django_filters.rest_framework import DjangoFilterBackend
from . import filters

# Create your views here.
def PosFilterRequire(request):
    all_city = models.Position.objects.values_list('city').distinct()
    all_workYear = ["1-3年", "3-5年", "应届毕业生", "5-10年", "1年以下", "10年以上"]
    all_skillLabels = models.Position.objects.values_list('skillLabels').distinct()
    all_education = ['小学', '初中', '高中', '大专', '本科', '硕士', '博士']
    city_list = [city[0] for city in all_city]
    skillLabels_list = {skill for skillLabels in all_skillLabels for skill in skillLabels[0].split(',')}
    return JsonResponse({'all_city': city_list, 'all_workYear': all_workYear, 'all_skillLabels': list(skillLabels_list), 'all_education': all_education})

def ComFilterRequire(request):
    all_companySize = ["15-50",  "50-150",  "150-500", "500-2000", "2000以上"]
    all_industryField = models.Company.objects.values_list('industryField').distinct()
    all_financeStage = ["A轮", "B轮", "C轮", "D轮", "E轮", "F轮"]
    all_legalize = ['未认证', '已认证']
    industryField_list = {field for industryField in all_industryField for field in industryField[0].split(',')}
    return JsonResponse({'all_companySize': all_companySize, 'all_industryField': list(industryField_list), 'all_financeStage': all_financeStage, 'all_legalize': all_legalize})

class ProvinceAPIView(APIView):
    def get(self, request):
        queryset = models.Province.objects.filter(is_show=True).order_by('orders').values('id', 'name')
        ser = serializers.ProvinceSerializers(instance=queryset, many=True)
        return Response(ser.data)

class JobsAPIView(ListAPIView):
    queryset = models.JobBigCategory.objects.filter(is_show=True).order_by('orders')
    serializer_class = serializers.CategorySerializers

class PositionListAPIView(ListAPIView):
    queryset = models.Position.objects.filter(is_show=True, is_delete=False).order_by('orders')
    serializer_class = serializers.PositionModelSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = filters.PositionFilter
    pagination_class = paginations.PositionListPagination

class PositionRetrieveAPIView(RetrieveAPIView):
    queryset = models.Position.objects.filter(is_show=True, is_delete=False)
    serializer_class = serializers.PositionRetrieveSerializer

class CompanyListAPIView(ListAPIView):
    queryset = models.Company.objects.filter(is_show=True, is_delete=False).order_by('orders')
    serializer_class = serializers.CompanyModelSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = filters.CompanyFilter
    pagination_class = paginations.CompanyListPagination

class CompanyRetrieveAPIView(RetrieveAPIView):
    lookup_field = 'companyId'
    queryset = models.Company.objects.filter(is_show=True, is_delete=False)
    serializer_class = serializers.CompanyRetrieveSerializer