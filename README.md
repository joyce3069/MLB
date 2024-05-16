![image](https://github.com/joyce3069/MLB/assets/84541926/eb6a1cde-f25a-497f-a9a0-d3f9c71e3ca8)

Connecting Python and PostgreSQL 


While we can do data importing, processing and exporting, some problems are most simply solved by writing Python scripts. 
Python can communicate with databases. In a sense, we use all the SQL statements as strings in Python and send them to our PostgreSQL server.
It is important to note that Python is just another client like psql or pgadmin. 
It makes a network connection to the database server using login credentials and sends SQL commands and receives results from the server.


Loading JSON from MLB API


In this tutorial, I will load the home run numbers and game day temperature of MLB 1991 year's JSON documents from the MLB API and store them in a table.
