<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>WelcomePage</title>
</head>
<body>

<%

response.setHeader("cache-control","no-cache,no-store,must-revalidate");

String username = session.getAttribute("username").toString();

if(session.getAttribute("username")== null){
	
	response.sendRedirect("login.jsp");
	
}

%>


   <h1>Welcomeee ${username}</h1>
   
   <br><br>
   
   <a href="videos.jsp">Videos here </a>
   <br><br>
   <form action="Logout">
   
   
   
    <input type="submit" value="logout">
   
   
   
   </form>
</body>
</html>