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

class PositionModelSerializer(serializers.ModelSerializer):
    skillLabels = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()

    def get_skillLabels(self, obj):
        skillLabelList = obj.skillLabels
        return skillLabelList.split(',')

    def get_education(self, obj):
        return obj.get_education_display()

    class Meta:
        model = models.Position
        fields = ['id', 'positionName', 'salary', 'workYear', 'education', 'skillLabels']

class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ['companyId', 'companyLogo', 'companyShortName', 'industryField', 'financeStage', 'companyIntro']

class CompanyRetrieveSerializer(serializers.ModelSerializer):
    companyIntro = serializers.SerializerMethodField()
    companyLabelList = serializers.SerializerMethodField()

    def get_companyIntro(self, obj):
        return obj.companyIntro.replace(r'\n', '<br>')

    def get_companyLabelList(self, obj):
        return obj.companyLabelList.split(',')

    class Meta:
        model = models.Company
        fields = ['companyLogo', 'companyShortName', 'companyFullName', 'industryField', 'financeStage', 'signature', 'company_size', 'companyLabelList', 'capital', 'createPerson', 'createPersonIntro', 'companyIntro', 'companySite', 'legalRepresentative', 'legalize', 'createTime', 'createPersonAvatar', 'latitude', 'longitude']

class PositionRetrieveSerializer(serializers.ModelSerializer):
    jobNature = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    company = serializers.SerializerMethodField()
    def get_company(self, obj):
        com = models.Company.objects.filter(companyId=obj.companyId).first()
        dic = {}
        dic['companyLogo'] = com.companyLogo.url
        dic['companyShortName'] = com.companyShortName
        dic['financeStage'] = com.financeStage
        dic['industryField'] = com.industryField
        dic['companySize'] = com.company_size
        dic['companySite'] = com.companySite
        return dic

    def get_jobNature(self, obj):
        return obj.get_jobNature_display()

    def get_education(self, obj):
        return obj.get_education_display()

    class Meta:
        model = models.Position
        fields = ['positionName', 'salary', 'workYear', 'city', 'district', 'subwayLine', 'stationName', 'education', 'jobNature', 'positionAdvantage', 'positionIntro', 'company']
