# DustProject
mysql_conn.jsp : 기본적인 웹,DB 환경설정후 정상적으로 연결구성을 확인하기 위한 테스트
insert.html : 웹서버상에서 외부에서 웹을 호출하여 데이터를 입력하는 화면
insert.jsp : 웹화면에 입력한 값을 DB에 저장하기 위한 소스
dustpm25.py : 미세먼지 데이터를 수집하여 DB에 저장, 공공기관 미세먼지 데이터를 API호출하여 xml 파싱후 DB에 저장 포함
data_read4.jsp : DB에 저장된 데이터를 불러오는 소스
view6.html : data_read4.jsp를 Ajax로 호출하여 구글차트를 이용하여 데이터를 그래프로 보여주는 
