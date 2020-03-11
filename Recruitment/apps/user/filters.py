from . import models
import django_filters

class NewsFilter(django_filters.FilterSet):
    user = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = models.News
        fields = ['id', 'user']

class ArticleFilter(django_filters.FilterSet):
    user = django_filters.NumberFilter(lookup_expr='exact')
    class Meta:
        model = models.Article
        fields = ['id', 'user']

class ResumeFilter(django_filters.FilterSet):
    user = django_filters.NumberFilter(lookup_expr='exact')
    class Meta:
        model = models.Resume
        fields = ['id', 'user']