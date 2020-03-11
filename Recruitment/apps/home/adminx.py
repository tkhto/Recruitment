import xadmin
from . import models

class ProvinceAdmin(object):
    list_display = ['name', 'orders', 'is_show']
xadmin.site.register(models.Province, ProvinceAdmin)

class JobBigCategoryAdmin(object):
    list_display = ['name', 'orders', 'is_show']
xadmin.site.register(models.JobBigCategory, JobBigCategoryAdmin)

class JobSubCategoryAdmin(object):
    list_display = ['name', 'orders', 'is_show']
xadmin.site.register(models.JobSubCategory, JobSubCategoryAdmin)

class CategoryAdmin(object):
    list_display = ['name', 'orders', 'is_show']
xadmin.site.register(models.Category, CategoryAdmin)

class CompanyAdmin(object):
    list_display = ['companyId', 'companyFullName', 'companySize']
xadmin.site.register(models.Company, CompanyAdmin)

class PositionAdmin(object):
    list_display = ['positionName', 'companyId', 'publisher', 'positionLabels']
xadmin.site.register(models.Position, PositionAdmin)