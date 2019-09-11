#%%

import psycopg2
import pprint

connection = psycopg2.connect(database="pythonspatial", user="postgres", password="postgres")

cursor = connection.cursor()


#%%

cursor.execute("SELECT * from art_pieces")
data=cursor.fetchall()

pprint.pprint(data)



#%%


