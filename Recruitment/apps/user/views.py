from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from Recruitment.libs.geetest import GeetestLib
from rest_framework.response import Response
from django.conf import settings
from . import serializers
from . import models
from rest_framework import status
import random
from django_redis import get_redis_connection
from Recruitment.libs.yuntongxun.sms import CCP


# Create your views here.
class ProvinceAPIView(APIView):
    def get(self, request):
        queryset = models.Province.objects.all().order_by('order').values('id', 'name')
        ser = serializers.ProvinceSerializers(instance=queryset, many=True)
        return Response(ser.data)

# 极验验证视图
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

# 发送短信视图
class SMSAPIView(APIView):
    def get(self,request,mobile):
        """
        短信发送接口
        url:
           /users/sms/(?P<mobile>1[3-9]\d{9})/
        """
        #1. 验证手机号码是否已经注册了
        try:
            models.Account.objects.get(mobile=mobile)
            return Response({"message":"对不起，当前手机已经被注册！"}, status=status.HTTP_400_BAD_REQUEST)
        except models.Account.DoesNotExist:
            pass

        #2. 验证手机是否在一分钟内曾经发送过短信了
        redis_conn = get_redis_connection("sms_code")
        ret = redis_conn.get("interval_%s" % mobile)
        if ret is not None:
            return Response({"message":"对不起，短信发送过于频繁！"})

        #3. 生成短信验证码
        sms_code = "%06d" % random.randint(100, 999999)

        #4. 保存短信验证码
        # redis_conn.setex("键","时间","值")
        # 使用redis提供的事务配合管道[pipeline]操作来保证多条命令要么一起执行，要么一起失败！
        # redis的事务也只能控制数据的修改，设置和删除操作，对于获取数据来说，没必要使用事务！
        pipe = redis_conn.pipeline() # 创建一个管道
        pipe.multi()  # 开启redis事务
        pipe.setex("sms_%s" % mobile, settings.SMS["sms_expire_time"], sms_code)
        pipe.setex("interval_%s" % mobile, settings.SMS["sms_interval_time"], "_")
        pipe.execute() # 执行redis事务

        #5. 发送短信
        ccp = CCP()
        ret = ccp.send_template_sms(mobile,[sms_code, settings.SMS["sms_expire_time"] // 60 ], settings.SMS["sms_template_id"])
        result = "短信发送失败" if ret else "短信发送成功"
        return Response({"message":result})