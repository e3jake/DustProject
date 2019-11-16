#!/usr/bin/python3
#-*- coding: utf-8 -*-
#http://tech.leotek.co.kr/2017/04/11/%EA%B3%B5%EA%B3%B5%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%8F%AC%ED%84%B8-%ED%95%9C%EA%B5%AD%ED%99%98%EA%B2%BD%EA%B3%B5%EB%8B%A8-%EB%8C%80%EA%B8%B0%EC%98%A4%EC%97%BC-api/
# openapi airkorea xml
#url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=u4Q%2FF%2BzFS1PHRIhVj2cJcxGP8J%2B5vOxCbaO039frcCGDEuD2km6rhbR2wZrwBrZtlLu2Z%2FbsqMHDVVGHwkq8ow%3D%3D&ver=1.3"
# openapi airkorea json
#url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=u4Q%2FF%2BzFS1PHRIhVj2cJcxGP8J%2B5vOxCbaO039frcCGDEuD2km6rhbR2wZrwBrZtlLu2Z%2FbsqMHDVVGHwkq8ow%3D%3D&ver=1.3&_returnType=json"

import xml.etree.ElementTree as ET
##import urllib2
import urllib.request
import datetime
import time
import sys
import pymysql
import random
now = time.localtime()

from random import *
chkpmValue = uniform(20.0,35.0)


#CurrentTime = datetime.datetime.now()
#CurrentTime = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
CurrentTime = "%04d-%02d-%02d %02d:00" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour)

# jongro-gu
URL1 = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=u4Q%2FF%2BzFS1PHRIhVj2cJcxGP8J%2B5vOxCbaO039frcCGDEuD2km6rhbR2wZrwBrZtlLu2Z%2FbsqMHDVVGHwkq8ow%3D%3D&ver=1.3"
# joong-gu
URL2 = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=%EC%A4%91%EA%B5%AC&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=u4Q%2FF%2BzFS1PHRIhVj2cJcxGP8J%2B5vOxCbaO039frcCGDEuD2km6rhbR2wZrwBrZtlLu2Z%2FbsqMHDVVGHwkq8ow%3D%3D&ver=1.3"


def db_insert(a, b, c) :
    # DB Connect
    conn = pymysql.connect(host='localhost', user='mgt', password='mgt',db='mysql', charset='utf8')
    curs = conn.cursor()
    
    sql = """insert into dust_airkorea(gps_id, pm10Value, pm25Value, datecreated) values(%s, %s, %s, now())""";
    curs.execute(sql, (a, b, c))
    conn.commit()
    conn.close()
    #@sys.exit(1)



#@print CurrentTime

if sys.version_info[0] == 3 :
    from urllib.request import urlopen # for Python 3.x
else:
    from urllib import urlopen # for Python 2.x

response = urlopen(URL1).read()
root = ET.fromstring(response)

if CurrentTime != 0:

    for item in root.iter('item') :
        dataTime = item.findtext('dataTime')
        if dataTime == CurrentTime :
            pm10Value = item.findtext('pm10Value')
            pm25Value = item.findtext('pm25Value')
            gpsid='KwangJu-BukGu'
            ##@print(dataTime, pm10Value, pm25Value)
            ##@sys.exit(1)

            if pm10Value != 0 and pm25Value != 0 :
                a = db_insert(gpsid, pm10Value, pm25Value)
            else : 
                sys.exit(1)
        else :
            sys.exit(1)

    else :
        sys.exit(1)
