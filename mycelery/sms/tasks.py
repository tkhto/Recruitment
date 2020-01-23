from mycelery.main import app
from .yuntongxun.sms import CCP
from django.conf import settings
import logging

log = logging.getLogger("django")

@app.task(name="send_sms_code")
def send_sms_code(mobile,sms_code):
    try:
        ccp = CCP()
        ccp.send_template_sms(mobile,[sms_code, settings.SMS["sms_expire_time"] // 60], settings.SMS["sms_template_id"])
        return True
    except:
        log.error("发送短信失败！用户手机：%s，验证码:%s" % (mobile, sms_code))
        return False