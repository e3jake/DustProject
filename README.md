# DustProject

쿼드콥터에 부착한 sds011 미세먼지 센서와 라즈베리파이 USB에 연결후 수집된 데이터를 클라우드 시스템으로 전송하여 DB에 데이터를 저장한다.(PM25, PM10)
수집된 데이터의 정합성을 검증하기 위해서 공공기관(airkorea.or.kr)의 데이터도 API로 주기적으로 호출하여 해당 지역의 미세먼지 데이터를 수집한다.
DB에 저장된 데이터는 구글차트와 연동하여 쿼드콥터에 부착한 미세먼지 센서 데이터와 공공기관 데이터를 시계열로 비교하여 보여준다

cronjob/dustpm25.py : 공공기관의 미세먼지 데이터를 API호출, 수집하여 XML파싱후 DB에 저장 및 수집된 데이터를 DB에 저장

etc/mysql_conn.jsp : 기본적인 웹,DB 환경설정후 정상적으로 연결구성을 확인하기 위한 테스트

webview/data_read4.jsp : DB에 저장된 데이터를 불러오는 소스

webview/view6.html : data_read4.jsp를 Ajax로 호출하여 구글차트를 이용하여 데이터를 그래프로 보여주는 

webview/insert.html : 웹서버상에서 외부에서 웹을 호출하여 데이터를 입력하는 화면 (웹상에서 데이터 값을 입력하고 DB에 저장하는 화면)

webview/insert.jsp : 웹화면에 입력한 값을 DB에 저장하기 위한 소스 (외부에서 web URL을 직접호출하여 post방식으로 DB를 저장하는 방법)

dust-sensor-read.py : 외부사이트에서 얻은 sds011 미세먼지 센서를 USB에 연결후 데이터 수신하는 프로그램

dust-sensor-read2.py : 외부사이트에서 얻은 sds011 미세먼지 센서를 USB에 연결후 데이터 수신하는 프로그램(날짜 PM25값 PM10값만 리턴)

sds-read.py : 외부사이트에서 얻은 sds011 미세먼지 센서를 USB에 연결후 데이터 수신하는 프로그램

sds-test.py : sds-read.py 소스에서 필요한 데이터만 날짜 시간을 포함하여 출력하는 수정된 프로그램

