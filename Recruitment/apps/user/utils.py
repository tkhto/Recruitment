from django.contrib.auth.backends import ModelBackend
from .models import Account

def jwt_response_payload_handler(token, user=None, request=None):
    """自定义jwt认证成功返回数据"""
    return {
        'token': token,
        'id': user.id,
        'username': user.username,
        'mobile': user.mobile,
        'nic_name': user.nic_name,
        'avatar': user.avatar.url,
        'user_type': user.user_type,
        'companyId': user.companyId
    }

def get_user_by_account(mobile):
    try:
        user = Account.objects.get(mobile=mobile)
    except Account.DoesNotExist:
        user = None
    return user

class UsernameMobileAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_account(username)
        if user is not None and user.check_password(password) and user.is_active:
            return user