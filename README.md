<h1>CSV to RDBMS</h2>


WARNING.*** This program will create/use a database named 'users'. If you have a database with this name change the dbname throughout the file 
to avoid errors, data loss and/or data corruption.

The program will create a database and table in MySQL. It will read the csv file in /input folder and add them to a MySQL or MariaDB database.
The CSV file can be updated and program will add new entries at each run of program.

<h2>Technical Assistance</h2>
User will need to pip install pandas and mysql.connector in order to run.

User will need to enter MySQL credentials in: 'host, username, password' for whatever instance(local,EC2,etc) they are using.

<h2>Technologies used</h2>
*Python3
*MySQL 8.0.27
*pandas 1.4.12


<h3>Side Notes</h3>
Project completed for Hexaware training 6/17/2022.
