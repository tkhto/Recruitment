import os
import sys
import django
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Recruitment.Recruitment.settings.dev")
django.setup() # os.environ['DJANGO_SETTINGS_MODULE']
# from home import models
# cate = models.Category.objects.all().values_list('name', 'parent')
# print(cate[0])