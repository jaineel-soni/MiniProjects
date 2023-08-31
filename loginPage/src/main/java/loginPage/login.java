package loginPage;

import java.io.IOException;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
@WebServlet("/Login")
public class login extends HttpServlet{
	
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
	
	        String uname = req.getParameter("uname");
	        String pass = req.getParameter("pass");
	        
	        HttpSession session = req.getSession();
	        session.setAttribute("username", uname);
	        
	        if(uname.equals("Jaineel") && pass.equals("Jaineel123")) {
	        	resp.sendRedirect("welcome.jsp");
	        }
	        else {
	        	resp.sendRedirect("login.jsp");
	        }
	        
	
	}

}
