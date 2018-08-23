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
        //String query = "select datecreated, drone_id, dust_id, gps_id, chkpmValue, pm25Value, pm10Value from dust order by datecreated desc";
        String query = "select datecreated as mdatecreated, chkpmValue, pm25Value, pm10Value from dust";

	//일별 평균값을 산출
        //String query = "select DATE_FORMAT(datecreated, '%Y-%m-%d') mdatecreated, avg(chkpmValue) chkpmValue, avg(pm25Value) pm25Value, avg(pm10Value) pm10Value from dust group by mdatecreated";

	PreparedStatement pstm = con.prepareStatement(query);
        rs = pstm.executeQuery(query);
        
        //ajax에 반환할 JSON 생성
        JSONObject responseObj = new JSONObject();
        JSONObject lineObj = null;
        
	DecimalFormat f1 = new DecimalFormat("");

    	while (rs.next()) {
            	String mdatecreated = rs.getString("mdatecreated");
            	float chkpmValue = rs.getFloat("chkpmValue");
            	float pm25Value = rs.getFloat("pm25Value");
            	float pm10Value = rs.getFloat("pm10Value");
 	    	lineObj = new JSONObject();
            	lineObj.put("mdatecreated", mdatecreated);
            	lineObj.put("chkpmValue", (int)chkpmValue);
            	lineObj.put("pm25Value", (int)pm25Value);
            	lineObj.put("pm10Value", (int)pm10Value);
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


