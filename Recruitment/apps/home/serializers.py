from rest_framework import serializers
from . import models

class ProvinceSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Province
        fields = ['id', 'name']

class CategorySerializers(serializers.ModelSerializer):
    sub_category = serializers.SerializerMethodField()

    def get_sub_category(self, obj):
        query_set = obj.sub_category.all()
        sub_dic = []
        for obj in query_set:
            cate = {
                'id': obj.id,
                'name': obj.name,
                'category': obj.category.all().values('id', 'name')
            }
            sub_dic.append(cate)
        return sub_dic

    class Meta:
        model = models.JobBigCategory
        fields = ["id", "name", "sub_category"]