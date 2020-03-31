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
    site_title = "Offend"  # 设置站点标题
    site_footer = "offer站有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠
xadmin.site.register(views.CommAdminView, GlobalSettings)

class NewsAdmin(object):
    list_display = ['user', 'content', 'pub_date', 'is_delete']
xadmin.site.register(models.News, NewsAdmin)

class NewsLikeAdmin(object):
    list_display = ['user', 'news_id']
xadmin.site.register(models.NewsLike, NewsLikeAdmin)

class NewsCommentsAdmin(object):
    list_display = ['user', 'parent', 'reply', 'news', 'create_time']
xadmin.site.register(models.NewsComments, NewsCommentsAdmin)

class ArticleAdmin(object):
    list_display = ['user', 'title', 'tag']
xadmin.site.register(models.Article, ArticleAdmin)

class ArticleLikeAdmin(object):
    list_display = ['user', 'article_id']
xadmin.site.register(models.ArticleLike, ArticleLikeAdmin)

class ArticleCommentsAdmin(object):
    list_display = ['user', 'parent', 'reply', 'article', 'create_time']
xadmin.site.register(models.ArticleComments, ArticleCommentsAdmin)

class ResumeAdmin(object):
    list_display = ['user', 'title', 'pub_date']
xadmin.site.register(models.Resume, ResumeAdmin)