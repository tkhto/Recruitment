from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.conf import settings
import re

class AuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        user = request.session.get('user')
        url = request.path_info

        for i in settings.WHITE_REGEX_URL_LIST:
            if re.match(r'^{}'.format(i), url):
                return
        return
