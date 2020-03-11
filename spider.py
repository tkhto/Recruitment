import pymysql
# import os
# os.environ.setdefaul t('DJANGO_SETTINGS_MODULE', 'Recruitment.settings.dev')
# import django
# django.setup()
# from Recruitment.apps.home import models
# from Recruitment.apps.user import models

import requests
from lxml import etree
import random
from faker import Faker
fake = Faker(locale='zh_CN')



def getCookie():
    url = "https://www.lagou.com/jobs/list_/p-city_0?px=new#filterBox"
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    res = requests.get(url=url, headers=headers)
    cookies = res.cookies.get_dict()
    COOKIE = ''
    for k, v in cookies.items():
        COOKIE += k + "=" + v + ";"
    return COOKIE

def createCompany(pos, headers):
    print('createCompany')
    com_res = requests.get(url=f"https://www.lagou.com/gongsi/{pos['companyId']}.html", headers=headers).text
    com_tree = etree.HTML(com_res)
    companyId = pos['companyId']
    companyShortName = pos['companyShortName']
    companyFullName = pos['companyFullName']
    companyLogo = pos['companyLogo']
    companySize = random.choice([0, 1, 2, 3, 4])
    industryField = pos['industryField']
    financeStage = random.choice([0, 1])
    companyLabelList = ','.join(pos['companyLabelList'])
    createPerson = fake.name()
    createPersonIntro = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
    companyIntroList = com_tree.xpath('//*[@id="company_intro"]/div[2]/div[1]/span[1]/p/text()')
    companyIntro = r'\n'.join(companyIntroList)
    capital = random.choice([20, 50, 100, 500, 1000, 2000, 5000, 10000])
    legalize = random.choice([0, 1])
    latitude = pos['latitude'] or '31.30444'
    longitude = pos['longitude'] or '121.45022'
    orders = 1
    is_show = 1
    is_delete = 0
    create_time = fake.future_datetime(end_date='+30d', tzinfo=None)
    update_time = fake.future_datetime(end_date='+30d', tzinfo=None)

    # print(companyId, companyShortName, companyFullName, companyLogo, companySize, industryField, financeStage, companyLabelList, companyIntro, createPerson, createPersonIntro, capital, legalize, latitude, longitude, orders, is_show, is_delete, create_time, update_time)
    sql = "INSERT INTO `home_company` (`companyId`, `companyShortName`, `companyFullName`, `companyLogo`, `companySize`, `industryField`, `financeStage`, `companyLabelList`, `companyIntro`, `createPerson`, `createPersonIntro`, `capital`, `legalize`, `latitude`, `longitude`, `orders`, `is_show`, `is_delete`, `create_time`, `update_time`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor = conn.cursor()
    cursor.execute(sql, (companyId, companyShortName, companyFullName, companyLogo, companySize, industryField, financeStage, companyLabelList, companyIntro, createPerson, createPersonIntro, capital, legalize, latitude, longitude, orders, is_show, is_delete, create_time, update_time))
    conn.commit()

def createPosition(pos, headers):
    print('createPosition')
    pos_res = requests.get(url=f"https://www.lagou.com/jobs/{pos['positionId']}.html", headers=headers).text
    pos_tree = etree.HTML(pos_res)
    pid = pos['positionId']
    positionName = pos['positionName']
    companyId = pos['companyId']
    publisher_id = pos['publisherId']
    firstTypeList = pos['firstType']
    firstType = ','.join(firstTypeList.split('|'))
    secondTypeList = pos['secondType']
    secondType = ','.join(secondTypeList.split('|'))
    thirdTypeList = pos['thirdType']
    thirdType = ','.join(thirdTypeList.split('|'))
    skillLabels = ','.join(pos['skillLables'])
    positionLabels = ','.join(pos['positionLables'])
    industryLabels = ','.join(pos['industryLables'])
    city = pos['city']
    district = pos['district'] or None
    salary = pos['salary']
    workYear = pos['workYear']
    jobNature = 1 if pos['jobNature'] == '全职' else 0
    education = random.randint(0, 6)
    isSchoolJob = pos['isSchoolJob']
    positionAdvantage = ','.join(pos['positionAdvantage'].split(' '))
    positionIntroList = pos_tree.xpath('//*[@id="job_detail"]/dd[2]/div/p/text()')
    positionIntro = '\n'.join(positionIntroList)
    subwayLine = pos['subwayline'] or None
    stationName = pos['stationname'] or None
    orders = 1
    is_show = 1
    is_delete = 0
    create_time = fake.future_datetime(end_date='+30d', tzinfo=None)
    update_time = fake.future_datetime(end_date='+30d', tzinfo=None)
    # models.Position.objects.create(id=id, positionName=positionName, companyId=companyId, publisher_id=publisher_id, firstType=firstType, secondType=secondType, thirdType=thirdType, skillLabels=skillLabels, positionLabels=positionLabels, industryLabels=industryLabels, city=city, district=district, salary=salary, workYear=workYear, positionIntro=positionIntro, jobNature=jobNature, education=education, isSchoolJob=isSchoolJob, positionAdvantage=positionAdvantage, subwayLine=subwayLine, stationName=stationName, orders=orders, is_show=is_show, is_delete=is_delete, create_time=create_time, update_time=update_time)
    # print(pid, positionName, companyId, publisher_id, firstType, secondType, thirdType, skillLabels, positionLabels, industryLabels, city, district, salary, workYear, positionIntro, jobNature, education, isSchoolJob, positionAdvantage, subwayLine, stationName, orders, is_show, is_delete, create_time, update_time)
    sql = "INSERT INTO `home_position` (`id`, `positionName`, `companyId`, `publisher_id`, `firstType`, `secondType`, `thirdType`, `skillLabels`, `positionLabels`, `industryLabels`, `city`, `district`, `salary`, `workYear`, `positionIntro`, `jobNature`, `education`, `isSchoolJob`, `positionAdvantage`, `subwayLine`, `stationName`, `orders`, `is_show`, `is_delete`, `create_time`, `update_time`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor = conn.cursor()
    cursor.execute(sql, (pid, positionName, companyId, publisher_id, firstType, secondType, thirdType, skillLabels, positionLabels, industryLabels, city, district, salary, workYear, positionIntro, jobNature, education, isSchoolJob, positionAdvantage, subwayLine, stationName, orders, is_show, is_delete, create_time, update_time))
    conn.commit()

def createAccount(pos):
    print('createAccount')
    uid = pos['publisherId']
    nic_name = fake.name()
    password = 'pbkdf2_sha256$150000$wHskUoUXKoO8$9y3qBvMuPYzb4PYM8AGJcIjNA0eJYRFeqQG+q4SKOBs='
    gender = random.choice([0, 1])
    mobile = fake.phone_number()
    avatar = 'media/avatar/avatar.jpg'
    birthday = fake.date(pattern='%Y-%m-%d', end_datetime=None)
    user_type = 1
    city = fake.city_name()
    companyId = pos['companyId']
    selfPosition = fake.job()
    work_status = 1
    username = mobile
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.company_email()
    is_staff = 0
    is_active = 1
    is_superuser = 0
    date_joined = fake.future_datetime(end_date='+30d', tzinfo=None)
    # models.Account.objects.create(id=id, password=password, nic_name=nic_name, gender=gender, mobile=mobile, avatar=avatar, birthday=birthday, user_type=user_type, city=city, companyId=companyId, selfPosition=selfPosition, work_status=work_status, username=username, first_name=first_name, last_name=last_name, email=email, is_staff=is_staff, is_active=is_active,date_joined=date_joined)
    # print(uid, password, nic_name, gender, mobile, avatar, birthday, user_type, city, companyId, selfPosition, work_status, username, first_name, last_name, email, is_staff, is_active,date_joined)
    sql = "INSERT INTO `user_account` (`id`, `password`, `nic_name`, `gender`,`mobile`, `avatar`, `birthday`, `user_type`, `city`, `companyId`, `selfPosition`, `work_status`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`,`date_joined`, `is_superuser`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (uid, password, nic_name, gender, mobile, avatar, birthday, user_type, city, companyId, selfPosition, work_status, username, first_name, last_name, email, is_staff, is_active,date_joined, is_superuser))
    except:
        return
    conn.commit()
    
def spider():
    for i in range(29, 100):
        url = "https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false"
        headers = {
            'Cookie': getCookie(),
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'Host': 'www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_/p-city_0?px=new',
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': None,
            'X-Requested-With': 'XMLHttpRequest',
        }
        data = {
            "first": "true",
            "pn": str(i),
            "kd": ""
        }
        print(i)
        res = requests.post(url=url, data=data, headers=headers).json()
        try:
            for pos in res['content']['positionResult']['result']:
                cursor = conn.cursor()
                sql = "SELECT `companyShortName` FROM `home_company` WHERE `companyId`=%s"
                cursor.execute(sql, (pos['companyId'],))
                result = cursor.fetchone()

                if result:
                    createAccount(pos)
                    createPosition(pos, headers)
                else:
                    createCompany(pos, headers)
                    createAccount(pos)
                    createPosition(pos, headers)
        except Exception as e:
            print('e', e, pos)
            # return
conn = pymysql.connect(host='localhost',port=3306,user='root',password='admin',db='Recruitment',charset='utf8mb4')

spider()