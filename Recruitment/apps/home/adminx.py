import xadmin
from . import models

class ProvinceAdmin(object):
    list_display = ['name', 'orders', 'is_show']
xadmin.site.register(models.Province, ProvinceAdmin)