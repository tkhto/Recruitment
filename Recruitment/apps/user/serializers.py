from . import models
from rest_framework import serializers
import re
from django_redis import get_redis_connection
from rest_framework_jwt.settings import api_settings

class AccountModelSerializer(serializers.ModelSerializer):
    """用户注册的序列化器"""
    # 字段声明
    sms_code = serializers.CharField(write_only=True, max_length=4, required=True, help_text="短信验证码")
    token = serializers.CharField(read_only=True, help_text="jwt的认证token")
    # 模型相关声明
    class Meta:
        model = models.Account
        fields = ["password", "sms_code", "token", "id", "username", "avatar", "companyId"]
        # 给模型序列化器进行额外声明
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"read_only": True},
        }

    # 验证相关代码
    def validate_mobile(self, data):
        """验证手机号码"""
        # 验证格式
        ret = re.match('^1[3-9]\d{9}$', data)
        if not ret:
            raise serializers.ValidationError("对不起，手机号码格式有误！")

        # 是否被注册了
        exists = models.Account.objects.filter(mobile=data).exists()
        if exists:
            raise serializers.ValidationError("对不起，手机号码已经被使用！")

        return data

    def validate(self, attrs):
        """验证数据"""
        # 短信验证码的逻辑
        mobile = attrs.get("mobile")
        client_sms_code = attrs.get("sms_code")
        redis_conn = get_redis_connection("sms_code")
        redis_sms_code = redis_conn.get(mobile)
        if redis_sms_code is None:
            raise serializers.ValidationError("短信验证码已经失效了！")

        # 2. 把用户提交的短信验证码和redis里面的进行对比是否正确
        if client_sms_code != redis_sms_code.decode():
            raise serializers.ValidationError("短信验证码错误！")

        # 3. 如果正确了，则删除掉redis中的验证码
        redis_conn.delete(mobile)
        return attrs

    # 保存数据的方法
    def create(self, validated_data):
        """创建数据"""
        mobile = validated_data.get("mobile")
        password = validated_data.get("password")
        try:
            # 添加用户方法 create_user
            user = models.Account.objects.create_user(mobile=mobile, password=password, username=mobile, user_type=1)
            # 手动生成jwt
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            user.token = jwt_encode_handler(payload)
            return user
        except:
            raise serializers.ValidationError("保存用户失败！")

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ["username", "nic_name", "avatar", "gender", "birthday", "intro", "site", "get_user_type_display", "city", "companyId", "selfPosition", "education", "work_status", "mobile", "email", "weibo", "github", "facebook", "twitter", "graduatedSchool", "specialty", "unifiedAdmission", "admissionTime", "graduationTime"]

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    userinfo = serializers.SerializerMethodField()

    def get_userinfo(self, obj):
        dic = {}
        dic['id'] = obj.user.id
        dic['avatar'] = obj.user.avatar.url
        dic['nic_name'] = obj.user.nic_name
        return dic

    class Meta:
        model = models.Article
        fields = ['id', 'title', 'tag', 'html_code', 'md_code', 'pub_date', 'update_date', 'read_num', 'is_delete', 'user', 'userinfo']

class ArticleCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleComments
        fields = "__all__"
    
class ResumeSerializer(serializers.ModelSerializer):
    userinfo = serializers.SerializerMethodField()
    isShow = serializers.SerializerMethodField()
    def get_userinfo(self, obj):
        dic = {}
        dic['avatar'] = obj.user.avatar.url
        dic['nic_name'] = obj.user.nic_name
        return dic

    def get_isShow(self, obj):
        return "1" if obj.is_show == True else "0"

    class Meta:
        model = models.Resume
        fields = ['id', 'title', 'html_code', 'md_code', 'pub_date', 'update_date', 'isShow', 'user', 'userinfo']
        
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeliveryRecord
        fields = "__all__"