from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView, Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import mixins
from . import models
from . import serializers
from . import paginations
from django_filters.rest_framework import DjangoFilterBackend
from . import filters
from rest_framework import status

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
    """获取省份列表"""
    def get(self, request):
        queryset = models.Province.objects.filter(is_show=True).order_by('orders').values('id', 'name')
        ser = serializers.ProvinceSerializers(instance=queryset, many=True)
        return Response(ser.data)

class JobsAPIView(ListAPIView):
    """查看所有职位分类菜单"""
    queryset = models.JobBigCategory.objects.filter(is_show=True).order_by('orders')
    serializer_class = serializers.CategorySerializers

class PositionListAPIView(ListAPIView):
    """查看职位列表"""
    queryset = models.Position.objects.filter(is_show=True, is_delete=False).order_by('orders')
    serializer_class = serializers.PositionModelSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = filters.PositionFilter
    pagination_class = paginations.PositionListPagination

class PsoitionViewset(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    """创建和删除职位"""
    queryset = models.Position.objects.filter(is_show=True, is_delete=False).order_by('orders')
    serializer_class = serializers.PositionViewsetSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = filters.PositionFilter
    pagination_class = paginations.PositionListPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class PositionAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            GenericViewSet):
    """查看职位详情"""
    queryset = models.Position.objects.filter(is_show=True, is_delete=False)
    serializer_class = serializers.PositionRetrieveSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class PositionRetrieveAPIView(mixins.RetrieveModelMixin, 
                            mixins.UpdateModelMixin, 
                            GenericViewSet):
    """更新职位详细"""
    queryset = models.Position.objects.filter(is_show=True, is_delete=False)
    serializer_class = serializers.PositionViewsetSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)  

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class CompanyListAPIView(ListAPIView):
    """查看所有公司列表"""
    queryset = models.Company.objects.filter(is_show=True, is_delete=False).order_by('orders')
    serializer_class = serializers.CompanyModelSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = filters.CompanyFilter
    pagination_class = paginations.CompanyListPagination

class CompanyRetrieveAPIView(RetrieveAPIView):
    """查看公司详情"""
    lookup_field = 'companyId'
    queryset = models.Company.objects.filter(is_show=True, is_delete=False)
    serializer_class = serializers.CompanyRetrieveSerializer

def search_company(request):
    """普通用户转为企业用户时 查询所在公司"""
    queryString = request.GET.get('queryString')
    data = models.Company.objects.filter(companyFullName__icontains=queryString).values('companyFullName')
    lst = []
    for i in data:
        lst.append({'value': i['companyFullName']})
    return JsonResponse({'status': 200, 'data': list(lst)})