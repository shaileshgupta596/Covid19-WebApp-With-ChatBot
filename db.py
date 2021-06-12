import mysql.connector

def dbconnect():
	conn= mysql.connector.connect(host="localhost",user="Lighthub",passwd="Lighthub",
	  database="lightproject")

	c= conn.cursor(buffered=True)
	return c,conn 


#CREATE TABLE covid19info (id INT AUTO_INCREMENT PRIMARY KEY,statename VARCHAR(50),
#totalcases INT,activecases INT,recoverdcase INT,cperm INT,datadate TIMESTAMP);