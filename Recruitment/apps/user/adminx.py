import xadmin
from xadmin import views
from . import models

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "链星招聘"  # 设置站点标题
    site_footer = "链星有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)

class ProvinceAdmin(object):
    list_display = ['name', 'order', 'status']
xadmin.site.register(models.Province, ProvinceAdmin)