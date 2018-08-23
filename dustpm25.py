#!/usr/bin/python
#-*- coding: utf-8 -*-
#http://tech.leotek.co.kr/2017/04/11/%EA%B3%B5%EA%B3%B5%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%8F%AC%ED%84%B8-%ED%95%9C%EA%B5%AD%ED%99%98%EA%B2%BD%EA%B3%B5%EB%8B%A8-%EB%8C%80%EA%B8%B0%EC%98%A4%EC%97%BC-api/
# openapi airkorea xml
#url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=u4Q%2FF%2BzFS1PHRIhVj2cJcxGP8J%2B5vOxCbaO039frcCGDEuD2km6rhbR2wZrwBrZtlLu2Z%2FbsqMHDVVGHwkq8ow%3D%3D&ver=1.3"
# openapi airkorea json
#url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=u4Q%2FF%2BzFS1PHRIhVj2cJcxGP8J%2B5vOxCbaO039frcCGDEuD2km6rhbR2wZrwBrZtlLu2Z%2FbsqMHDVVGHwkq8ow%3D%3D&ver=1.3&_returnType=json"

import xml.etree.ElementTree as ET
import urllib2
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

url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=u4Q%2FF%2BzFS1PHRIhVj2cJcxGP8J%2B5vOxCbaO039frcCGDEuD2km6rhbR2wZrwBrZtlLu2Z%2FbsqMHDVVGHwkq8ow%3D%3D&ver=1.3"

tree = ET.ElementTree(file=urllib2.urlopen(url))
root = tree.getroot()

def db_insert(a, b, c) :
    # DB Connect
    conn = pymysql.connect(host='localhost', user='mgt', password='mgt',db='mysql', charset='utf8')
    curs = conn.cursor()

    sql = """insert into dust(drone_id, dust_id, gps_id, chkpmValue, pm25Value, pm10Value, datecreated) values('drone01', 'dust01', 'Eulgiro4ga', %s, %s, %s, now())""";
    curs.execute(sql, (a, b, c))
    conn.commit()
    conn.close()
    sys.exit(1)

#print CurrentTime
if CurrentTime > 0 :

    for i in root.iter("item") :
        i.dataTime = i.findtext("dataTime")
        if i.dataTime == CurrentTime :
            i.pm10Value = i.findtext("pm10Value")
            i.pm25Value = i.findtext("pm25Value")
            #print i.dataTime, i.pm10Value, i.pm25Value

	    if i.pm25Value > 0 and i.pm10Value > 0 :
	        a = db_insert(chkpmValue, i.pm25Value, i.pm10Value)
	    else : 
	        sys.exit(1)
	else :
	    sys.exit(1)

else :
    sys.exit(1)
