<%@page import="java.text.DecimalFormat"%>
<%@page import="java.sql.*"%>
<%@page import="java.util.*"%>
<%@page import="org.json.simple.JSONObject"%>
<%
    //커넥션 선언
    Connection con = null;

    try {
        //드라이버 호출, 커넥션 연결
        Class.forName("com.mysql.jdbc.Driver").newInstance();
        con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mysql?autoReconnect=true&useSSL=false", "mgt", "mgt");

    	ResultSet rs = null;
        //DB에서 뽑아온 데이터(JSON) 을 담을 객체. 후에 responseObj에 담기는 값
        List dustlist = new LinkedList();
 
	//전체 데이터 
        //String query = "select datecreated as mdatecreated, pm10Value, pm25Value from dust_airkorea where gps_id='JongRo-Gu'";
        //String query = "select a.datecreated as mdatecreated, b.pm25Value as Drnpm25Value, a.pm10Value as pm10Value, a.pm25Value as pm25Value from dust_airkorea a, dust_drone b where b.gps_id='JongRo-Gu'";

	//시간대별  평균값을 산출
	String query = "select DATE_FORMAT(a.datecreated, '%Y-%m-%d %H:00:00') mdatecreated, avg(a.pm10Value) as Drnpm10Value, avg(a.pm25Value) as Drnpm25Value , avg(b.pm10Value) as pm10Value, avg(b.pm25Value) as pm25Value from dust_drone a inner join dust_airkorea b where a.gps_id=b.gps_id and DATE_FORMAT(a.datecreated,'%Y-%m-%d %H:00')=DATE_FORMAT(b.datecreated,'%Y-%m-%d %H:00') group by mdatecreated";


	PreparedStatement pstm = con.prepareStatement(query);
        rs = pstm.executeQuery(query);
        
        //ajax에 반환할 JSON 생성
        JSONObject responseObj = new JSONObject();
        JSONObject lineObj = null;
        
	DecimalFormat f1 = new DecimalFormat("");

    	while (rs.next()) {
            	String mdatecreated = rs.getString("mdatecreated");
            	float Drnpm10Value = rs.getFloat("Drnpm10Value");
            	float Drnpm25Value = rs.getFloat("Drnpm25Value");
            	float pm10Value = rs.getFloat("pm10Value");
            	float pm25Value = rs.getFloat("pm25Value");
 	    	lineObj = new JSONObject();
            	lineObj.put("mdatecreated", mdatecreated);
            	lineObj.put("Drnpm10Value", (int)Drnpm10Value);
            	lineObj.put("Drnpm25Value", (int)Drnpm25Value);
            	lineObj.put("pm10Value", (int)pm10Value);
            	lineObj.put("pm25Value", (int)pm25Value);
            	dustlist.add(lineObj);
        } 

    responseObj.put("dustlist", dustlist);
        out.print(responseObj.toString());
 
    } catch (Exception e) {
        e.printStackTrace();
    } finally {
        if (con != null) {
            try {
                con.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
 
    }
%>


