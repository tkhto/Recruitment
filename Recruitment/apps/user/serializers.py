from . import models
from rest_framework import serializers
import re

class ProvinceSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Province
        fields = ['id', 'name']

class AccountModelSerializer(serializers.ModelSerializer):
    """用户注册的序列化器"""
    # 字段声明
    sms_code = serializers.CharField(write_only=True, max_length=6, required=True, help_text="短信验证码")
    token = serializers.CharField(read_only=True, help_text="jwt的认证token")
    # 模型相关声明
    class Meta:
        model = models.Account
        fields = ["mobile","password","sms_code","id","username","token"]
        # 给模型序列化器进行额外声明
        extra_kwargs = {
            "password":{"min_length": 6, "write_only": True, },
            "mobile":{"write_only":True},
            "username":{"read_only":True},
        }

    # 验证相关代码
    def validate_mobile(self,data):
        """验证手机号码"""
        # 验证格式
        ret = re.match('1[3-9]\d{9}',data)
        if not ret:
            raise serializers.ValidationError("对不起，手机号码格式有误！")

        # 是否被注册了
        try:
            models.Account.objects.get(mobile=data)
            raise serializers.ValidationError("对不起，手机号码已经被使用！")
        except models.Account.DoesNotExist:
            pass

        return data

    def validate(self, attrs):
        """验证数据"""
        # todo 补充短信验证码的逻辑
        pass

        return attrs

    # 保存数据的方法
    def create(self, validated_data):
        """创建数据"""
        mobile = validated_data.get("mobile")
        password = validated_data.get("password")
        try:
            # 添加用户方法 create_user
            user = models.Account.objects.create_user(mobile=mobile,password=password,username=mobile)

            # 手动生成jwt
            from rest_framework_jwt.settings import api_settings
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            user.token = jwt_encode_handler(payload)
            return user
        except:
            raise serializers.ValidationError("保存用户失败！")
        