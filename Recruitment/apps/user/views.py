import os
import time
import random
import json
import re
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView
from Recruitment.libs.geetest import GeetestLib
from rest_framework.response import Response
from rest_framework import mixins
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from . import serializers
from . import models
from . import filters
from . import paginations
from rest_framework import status
from django_redis import get_redis_connection
from django_filters.rest_framework import DjangoFilterBackend
from Recruitment.utils.tencent.sms import send_sms_single
from home.models import Position, Company
# Create your views here.


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
        if result:
            result = {"status": "success"} 
        else:
            result = {"status": "fail"}
        return Response(result)

class AccountAPIView(CreateAPIView):
    """用户管理"""
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountModelSerializer

@csrf_exempt
def change_user_type(request):
    """切换用户类型为普通用户"""
    data = json.loads(request.body.decode())
    user_id = data.get('user_id')
    mobile = data.get('mobile')
    user_obj = models.Account.objects.filter(pk=user_id, mobile=mobile).first()
    if not user_obj:
        return JsonResponse({'status': 400})
    user_obj.user_type = "0" if user_obj.user_type == "1" else "1"
    user_obj.companyId = None
    user_obj.save()
    Position.objects.filter(publisher_id=user_id).update(is_delete=1, is_show=0)
    return JsonResponse({'status': 200})

class AccountViewset(GenericViewSet, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        # serializer = self.get_serializer(instance, data=json.loads(request.body), partial=partial)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

class NewsViewset(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = models.News.objects.filter(is_delete=0).order_by('-pub_date')
    serializer_class = serializers.NewSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = filters.NewsFilter
    pagination_class = paginations.NewsPagination

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

class ArticleViewset(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = models.Article.objects.filter(is_delete=0).order_by('-pub_date')
    serializer_class = serializers.ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = filters.ArticleFilter
    pagination_class = paginations.ArticlePagination

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

class ArticleRetrieve(GenericViewSet, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        obj = serializer.data
        obj.pop('pub_date')
        obj.pop('update_date')
        obj.pop('is_delete')
        return JsonResponse({'result': obj})

class ArticleCommentsViewset(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = models.ArticleComments.objects.all()
    serializer_class = serializers.ArticleCommentsSerializer
    def getUserInfo(self, comment):
        dic = {}
        dic['cid'] = comment.pk
        dic['content'] = comment.content
        dic['create_time'] = comment.create_time
        dic['reply'] = {}
        reply_obj = models.ArticleComments.objects.filter(pk=comment.reply).first()
        dic['reply']['uid'] = reply_obj.user.pk
        dic['reply']['nic_name'] = reply_obj.user.nic_name
        dic['user'] = {}
        dic['user']['uid'] = comment.user.pk
        dic['user']['avatar'] = comment.user.avatar.url
        dic['user']['nic_name'] = comment.user.nic_name

        return dic

    def list(self, request, *args, **kwargs):
        comment_dic = {}
        comment_list = self.queryset.filter(article_id=kwargs['aid'])
        for comment in comment_list:
            if comment.parent:
                comment_dic[comment.parent].setdefault('sub_comment', [])
                comment_dic[comment.parent]['sub_comment'].append(self.getUserInfo(comment))
            else:
                comment_dic[comment.pk] = {}
                comment_dic[comment.pk]['cid'] = comment.pk
                comment_dic[comment.pk]['content'] = comment.content
                comment_dic[comment.pk]['create_time'] = comment.create_time
                comment_dic[comment.pk]['aid'] = comment.article_id
                comment_dic[comment.pk]['user'] = {}
                comment_dic[comment.pk]['user']['uid'] = comment.user.id
                comment_dic[comment.pk]['user']['avatar'] = comment.user.avatar.url
                comment_dic[comment.pk]['user']['nic_name'] = comment.user.nic_name
        return JsonResponse(comment_dic)

class ResumeViewset(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = models.Resume.objects.filter(is_delete=0).order_by('-pub_date')
    serializer_class = serializers.ResumeSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = filters.ResumeFilter
    pagination_class = paginations.ResumePagination

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

class ResumeRetrieve(GenericViewSet, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    queryset = models.Resume.objects.all()
    serializer_class = serializers.ResumeSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

        
@csrf_exempt
def avatar_upload(request):
    filename = str(int(time.time()) + random.randint(1, 100)) + ".jpg"
    myFile =request.FILES.get("file", None) 
    destination = open(os.path.join("./Recruitment/uploads/avatar",filename),'wb+')    # 打开特定的文件进行二进制的写操作
    for chunk in myFile.chunks():      # 分块写入文件
        destination.write(chunk)
    destination.close()
    return JsonResponse({"url": f"avatar/{filename}"})

@csrf_exempt
def user_auth(request):
    comapanyName = request.GET.get('name')
    email = request.GET.get('email')
    user_id = request.GET.get('uid')
    mobile = request.GET.get('mobile')
    company_obj = Company.objects.filter(companyFullName=comapanyName, companyEmail__icontains=email).first()
    if not company_obj:
        return JsonResponse({'status': 400, 'msg': "该公司或邮箱不存在"})
    user_obj = models.Account.objects.filter(pk=user_id, mobile=mobile).first()
    if not user_obj:
        return JsonResponse({'status': 400, 'msg': "该用户不存在"})
    user_obj.user_type = "1"
    user_obj.companyId = company_obj.companyId
    user_obj.save()
    return JsonResponse({'status': 200, 'msg': "切换切页用户成功"})

class DeliveryViewset(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    GenericViewSet):
    queryset = models.DeliveryRecord.objects.filter(isdelivery_delete=0).order_by('create_time')
    serializer_class = serializers.DeliverySerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

def delivery_record(request, user):
    """获取投递记录"""
    data = models.DeliveryRecord.objects.filter(isdelivery_delete=False, user_id=user).values('pk', 'create_time', 'position__id', 'position__positionName', 'status')
    return JsonResponse({'status': 200, 'data': list(data)})

def received_record(request, user):
    """获取接收投递记录"""
    data = models.DeliveryRecord.objects.filter(isreceiver_delete=False,position__publisher_id=user).values('pk', 'user__nic_name', 'user__resume__id', 'user_id', 'position_id', 'status', 'create_time')
    return JsonResponse({'status': 200, 'data': list(data)})

def received_change(request, pk):
    """改变投递记录状态"""
    obj = models.DeliveryRecord.objects.filter(pk=pk).first()
    obj.status = 1
    obj.save()
    return JsonResponse({'status': 200})

def delivery_delete(request, pk):
    """删除投递记录"""
    user_type = request.GET.get('type')
    obj = models.DeliveryRecord.objects.filter(pk=pk).first()
    if user_type == 'receiver':
        obj.isreceiver_delete = 1
    elif user_type == 'delivery':
        obj.isdelivery_delete = 1
    obj.save()
    return JsonResponse({'status': 200})

# 发送短信视图
class SMSAPIView(APIView):
    def get(self, request):
        """
        短信发送接口
        """
        # 验证手机号是否正确
        mobile = request.GET.get('mobile')
        reg = "1[3|4|5|7|8][0-9]{9}"
        if not re.findall(reg, mobile):
            return Response({'status': False, 'msg': '手机号格式不正确'})

        # 验证模版id
        tpl = request.GET.get('tpl')
        template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
        if not template_id:
            return Response({'status': False, 'msg': '模版id不存在'})

        # 验证手机号码是否已经注册了
        exists = models.Account.objects.filter(mobile=mobile).exists()
        if exists:
            return Response({'status': False, "message": "对不起，当前手机已经被注册！"})

        # 验证手机是否在一分钟内曾经发送过短信了
        redis_conn = get_redis_connection("sms_code")
        # 还剩多久过期
        ret = redis_conn.ttl(mobile) 
        if ret >= 0:
            return Response({"status": False, "message": f"对不起，请在{ret}秒后重试"})

        # 生成短信验证码
        sms_code = random.randrange(1000, 9999)

        # 发送短信
        sms = send_sms_single(mobile, template_id, [sms_code, ])
        if sms['result'] != 0:
            return Response({'status': False, 'msg': '短信发送失败'})

        # 保存短信验证码
        redis_conn.set(mobile, sms_code, ex=settings.SMS_EXPIRE)
        return Response({'status': 0, "message": "验证码正发往您的手机, 请留心"})