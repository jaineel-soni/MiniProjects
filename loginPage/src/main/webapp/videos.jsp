<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>VideosPage</title>
</head>
<body>

<%
response.setHeader("cache-control","no-cache,no-store,must-revalidate");

String username = session.getAttribute("username").toString();

if(session.getAttribute("username")== null){
	
	response.sendRedirect("login.jsp");
	
}

%>
Welcome to the videos page

<br><br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/OuBUUkQfBYM?si=MEvOvpmo4te3dhaH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<br>
<form action="Logout">
   
   
   
    <input type="submit" value="logout">
   
   
   
   </form>
</body>
</html>