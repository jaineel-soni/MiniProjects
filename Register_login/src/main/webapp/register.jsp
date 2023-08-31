<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Registration form</title>
</head>
<body>
<form action="regForm" method="post">

Name: <input type="text" name="Name"><br><br>
Email: <input type="email" name="Email"><br><br>
Password: <input type="password" name="Password"><br><br>
City: <select name="City">
     
      <option>Ahmedabad</option>
      <option>Mumbai</option>
      <option>Pune</option>
      <option>Bangalore</option>
      <option>Chennai</option> 
      
      </select>
<br><br>
Gender: <input type="radio" name="gender1" value="Male">Male<input type="radio" name="gender1" value="Female">Female <br><br>
<input type="submit" value="register">
</form>
</body>
</html>