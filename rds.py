## importing packages
import mysql.connector
import pandas as pd

## Connection to MySQL: user and password credentials need to be used.
connection= mysql.connector.connect(
    host='localhost',
    user='root',
    password='fake_password'
)

##Setup for MySQL operations
statement=connection.cursor()
# HOW TO USE example ---->   statement.execute('SQL QUERY')

## CREATE DATABASE and USE
statement.execute('CREATE DATABASE users')
statement.execute('USE users')

## Create Table
statement.execute('''
    CREATE TABLE user_info (
        No INT PRIMARY KEY, 
        Name_id VARCHAR(55), 
        email VARCHAR(255)
        )
    ''')

## Importing CSV file via Pandas
    ## may need to use absolute path for file location if you moved input folder.
data=pd.read_csv(r'input\a.csv')
df=pd.Dataframe(data)

## INSERT VALUES into table using pandas
for row in df.intertuples():
    statement.execute('''
    INSERT INTO user_info(No, Name_id, email) 
    VALUES (?,?,?)
    ''',
    row.No,
    row.Name_id,
    row.email
    )

## Show results
result=statement.execute('Select * from users')
print(result)

connection.commit()
connection.close()