## importing packages
import mysql.connector
import pandas as pd
try:
    ## Connection to MySQL: user and password credentials need to be used.
    print('Attempting to connect to MariaDB/MySQL')
    connection= mysql.connector.connect(host="127.0.0.1", user="root", password="")
    ##Setup for RDS operatiosn
    statement=connection.cursor()
except mysql.connector.errors.ProgrammingError:
    print('Connection failed check instance connection and credentials.')
    pass
## CREATE DATABASE and USE
try:
    statement.execute('CREATE DATABASE users;')
    print('Database \'users\' was created successfully.')
    statement.execute('USE users;')
except mysql.connector.errors.DatabaseError:
    print('Loading database \'users\'.')
    statement.execute('USE users;')
    pass
try:   
    ## Create Table
    statement.execute('CREATE TABLE user_info (No INT PRIMARY KEY,  Name_id VARCHAR(55), email VARCHAR(255));')
except mysql.connector.errors.ProgrammingError:
    print('Table exist already.')
    check=True
    while check:
        choice=input("Drop table user_info that already exists and create new one? \nType \'yes\' or \'no\'.\n").upper()
        if choice == 'YES':
            #Drop table if exist
            statement.execute('DROP TABLE IF EXISTS user_info;')
            statement.execute('CREATE TABLE user_info (No INT PRIMARY KEY,  Name_id VARCHAR(55), email VARCHAR(255));')
            check=False
        elif choice == 'NO':
            print('Using existing table.')
            check=False
            pass
        else:
            print('Invalid input try again.')
## Importing CSV file via Pandas
data=pd.read_csv(r'input\a.csv')
df=pd.DataFrame(data)
## INSERT VALUES into table using pandas dataFrame object
for row in df.itertuples():
    try:
        insert='INSERT INTO user_info(No, Name_id, email) VALUES (%s,%s,%s)'  
        statement.execute(insert,(row[1],row[2],row[3]))
    except mysql.connector.errors.IntegrityError:
         pass
print('All proccess completed. Shutting down instance.') 
statement.close()
connection.commit()
connection.close()