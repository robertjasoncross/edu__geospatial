import psycopg2
connection = psycopg2.connect(host='localhost', user='{user}',
	password='{password}', port="5432")
connection.autocommit = True
cursor = connection.cursor()
cursor.execute('CREATE DATABASE chapter12')
connection.close() 


connection = psycopg2.connect(dbname='ch12', host='localhost',
 user='{user}', password='{password}', port="5432")
cursor = connection.cursor()
connection.autocommit = True
cursor.execute('CREATE EXTENSION postgis')
connection.close() 

