import os
import time
import random
import json
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
import random
from django_redis import get_redis_connection
from django_filters.rest_framework import DjangoFilterBackend
# from mycelery.sms.yuntongxun.sms import CCP
from mycelery.sms.tasks import send_sms_code

# Create your views here.

#TODO 短信验证码
#TODO xadmin

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

# 发送短信视图
class SMSAPIView(APIView):
    def get(self, request, mobile):
        """
        短信发送接口
        url:
           /users/sms/(?P<mobile>1[3-9]\d{9})/
        """
        # 1. 验证手机号码是否已经注册了
        try:
            models.Account.objects.get(mobile=mobile)
            return Response({"message": "对不起，当前手机已经被注册！"}, status=status.HTTP_400_BAD_REQUEST)
        except models.Account.DoesNotExist:
            pass

        # 2. 验证手机是否在一分钟内曾经发送过短信了
        redis_conn = get_redis_connection("sms_code")
        # code = redis_conn.get("sms_%s" % mobile)
        ret = redis_conn.ttl("interval_%s" % mobile)

        if ret >= 0:
            return Response({"message": f"对不起，请在{ret}秒后重试"})

        # 3. 生成短信验证码
        sms_code = "%06d" % random.randint(100, 999999)
        send_sms_code.delay(mobile, sms_code)

        # 4. 保存短信验证码
        # redis_conn.setex("键","时间","值")
        # 使用redis提供的事务配合管道[pipeline]操作来保证多条命令要么一起执行，要么一起失败！
        # redis的事务也只能控制数据的修改，设置和删除操作，对于获取数据来说，没必要使用事务！
        pipe = redis_conn.pipeline()  # 创建一个管道
        pipe.multi()  # 开启redis事务
        pipe.setex("sms_%s" % mobile, settings.SMS["sms_expire_time"], sms_code)
        pipe.setex("interval_%s" % mobile, settings.SMS["sms_interval_time"], '_')
        pipe.execute() # 执行redis事务
        result = "验证码正发往您的手机, 请留心"
        return Response({'status': 0, "message": result})
        # else:
        #     result = "验证码发送失败, 请重试"
        #     return Response({'status': -1, "message": result})
