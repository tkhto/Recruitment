from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from Recruitment.libs.geetest import GeetestLib
from rest_framework.response import Response
from django.conf import settings
from . import serializers
from . import models

# Create your views here.
class ProvinceAPIView(APIView):
    def get(self, request):
        queryset = models.Province.objects.all().order_by('order').values('id', 'name')
        ser = serializers.ProvinceSerializers(instance=queryset, many=True)
        return Response(ser.data)

class GeetestCapchaAPIView(APIView):
    def get(self, request):
        """生成验证码的流水号"""
        user_id = 'test'
        gt = GeetestLib(settings.GEETEST["pc_geetest_id"], settings.GEETEST["pc_geetest_key"])
        status = gt.pre_process(user_id)
        response_str = gt.get_response_str()
        import json
        response = json.loads(response_str)
        return Response(response)

    def post(self,request):
        """校验验证码的结果"""
        gt = GeetestLib(settings.GEETEST["pc_geetest_id"], settings.GEETEST["pc_geetest_key"])
        challenge = request.data.get(gt.FN_CHALLENGE, '')
        validate = request.data.get(gt.FN_VALIDATE, '')
        seccode = request.data.get(gt.FN_SECCODE, '')
        result = gt.failback_validate(challenge, validate, seccode)
        result = {"status": "success"} if result else {"status": "fail"}
        return Response(result)

class AccountAPIView(CreateAPIView):
    """用户管理"""
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountModelSerializer

