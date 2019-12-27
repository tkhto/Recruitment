# 主程序
from celery import Celery
# 创建celery实例对象
app = Celery("luffy")

#1.1 如果celery需要在任务调用其它框架的内部对象，则需要进行相应的框架初始化
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Recruitment.settings.dev')
django.setup()

# 通过app对象加载配置
app.config_from_object("mycelery.config")

# 自动搜索并加载任务
# 参数必须必须是一个列表，里面的每一个任务都是任务的路径名称
# app.autodiscover_tasks(["任务1","任务2",....])
app.autodiscover_tasks(["mycelery.sms","mycelery.cache"])

# 启动Celery的命令
# 强烈建议切换目录到项目的根目录下启动celery!!
# celery -A mycelerymain worker --loglevel=info