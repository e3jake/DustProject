<%@page import="java.text.DecimalFormat"%>
<%@page import="java.sql.*"%>
<%@page import="java.util.*"%>
<%@page import="org.json.JSONObject"%>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
<head>
<body>
<%
    request.setCharacterEncoding("utf-8");
    String drone_id=request.getParameter("drone_id");
    String dust_id=request.getParameter("dust_id");
    String gps_id=request.getParameter("gps_id");
    String result=request.getParameter("result");
    String std_result=request.getParameter("std_result");

    //커넥션 선언
    Connection con = null;
    int n=0;

    try {
        //드라이버 호출, 커넥션 연결
        Class.forName("com.mysql.jdbc.Driver").newInstance();
        con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mysql?autoReconnect=true&useSSL=false", "mgt", "mgt");
        String query = "insert into dust(drone_id, dust_id, gps_id, result, std_result, datecreated) values(?,?,?,?,?,now())";
    	PreparedStatement pstmt = con.prepareStatement(query);

        pstmt=con.prepareStatement(query);
	pstmt.setString(1,drone_id);
	pstmt.setString(2,dust_id);
	pstmt.setString(3,gps_id);
	pstmt.setString(4,result);
	pstmt.setString(5,std_result);

	n=pstmt.executeUpdate();

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

<script type="text/javascript">
    if(<%=n%> > 0){
	alert("success...");
    }else {
	alert("fail ...");
    }
</script>
</body>
</html>
