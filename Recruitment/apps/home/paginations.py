from rest_framework.pagination import PageNumberPagination

class PositionListPagination(PageNumberPagination):
    """工作列表的分页器"""
    page_query_param = "page"  # 页码在地址栏中的参数名称
    page_size_query_param = "size"  # 单页数据量在地址栏上的参数名称
    page_size = 16  # 默认的单页数据量
    max_page_size = 100  # 允许客户端通过参数调整的最大的单页数据量

class CompanyListPagination(PageNumberPagination):
    """公司列表的分页器"""
    page_query_param = "page"  # 页码在地址栏中的参数名称
    page_size_query_param = "size"  # 单页数据量在地址栏上的参数名称
    page_size = 8  # 默认的单页数据量
    max_page_size = 100  # 允许客户端通过参数调整的最大的单页数据量