from . import models
import django_filters

class PositionFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='exact')
    workYear = django_filters.CharFilter(lookup_expr='exact')
    education = django_filters.NumberFilter(lookup_expr='exact')
    skillLabels = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Position
        fields = ['city', 'workYear', 'education', 'skillLabels', 'publisher', 'companyId']

class CompanyFilter(django_filters.FilterSet):
    companySize = django_filters.NumberFilter(lookup_expr='exact')
    industryField = django_filters.CharFilter(lookup_expr='icontains')
    financeStage = django_filters.CharFilter(lookup_expr='exact')
    legalize = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = models.Company
        fields = ['companySize', 'industryField', 'financeStage', 'legalize']