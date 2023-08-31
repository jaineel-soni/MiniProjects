package jaineel.com;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import com.mysql.cj.protocol.Resultset;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
@WebServlet("/login")
public class login extends HttpServlet{
	
      @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    	String myemail = req.getParameter("Email");
    	String mypass = req.getParameter("Password");
    	
    	PrintWriter outPrintWriter = resp.getWriter();
    	
    	try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/regForm","root","root123");
			
			PreparedStatement ps = con.prepareStatement("select * from register where email=? and password=? ");
			ps.setString(1, myemail);
			ps.setString(2, mypass);
			
			ResultSet rs = ps.executeQuery();
			
			if(rs.next()) {
				resp.setContentType("text/html");
				HttpSession session = req.getSession();
				session.setAttribute("session_name", rs.getString("name"));
				RequestDispatcher rd = req.getRequestDispatcher("/profile.jsp");
				rd.include(req, resp);
			}
			else {
				outPrintWriter.print("<h2 style='color:red'>Email and Password incorrect</h2>");
				resp.setContentType("text/html");
				
				RequestDispatcher rd = req.getRequestDispatcher("/login.jsp");
				rd.include(req, resp);
			}
		} 
    	catch (Exception e) {
			outPrintWriter.print("<h2 style='color:red'>Email and Password incorrect</h2> "+e.getMessage());
			resp.setContentType("text/html");
			
			RequestDispatcher rd = req.getRequestDispatcher("/login.jsp");
			rd.include(req, resp);
		
		}
    }
	
}
