from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView
from . import models
from . import serializers
import requests
from lxml import etree

# Create your views here.
class ProvinceAPIView(APIView):
    def get(self, request):
        queryset = models.Province.objects.filter(is_show=True).order_by('orders').values('id', 'name')
        ser = serializers.ProvinceSerializers(instance=queryset, many=True)
        return Response(ser.data)

class JobsAPIView(ListAPIView):
    queryset = models.JobBigCategory.objects.filter(is_show=True).order_by('orders')
    serializer_class = serializers.CategorySerializers