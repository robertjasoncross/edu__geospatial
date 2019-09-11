#%%
import psycopg2

connection = psycopg2.connect(database="pythonspatial", user="postgres", password="postgres")

cursor = connection.cursor()

#%%

#cursor.execute("CREATE TABLE art_pieces (id SERIAL PRIMARY KEY,code VARCHAR(255), location GEOMETRY)" )
#connection.commit()

#%%

import requests
import pprint
#pp = pprint.PrettyPrinter(indent=1)

url="http://coagisweb.cabq.gov/arcgis/rest/services/public/PublicArt/MapServer/0/query"
params={"where": "1=1","outFields":"*","outSR":"4326", "f":"json"}

r=requests.get(url, params=params)
data = r.json()
data["features"][0]

pprint.pprint(data)

#%%

for a in data["features"]:
    code=a["attributes"]["ART_CODE"]
    pt=Point(float(a["geometry"]["x"]), float(a["geometry"]["y"]))
    if a["geometry"]["x"] == 'NaN':
        pass
    else:
        cursor.execute("INSERT INTO art_pieces (code, location) VALUES ({}, ST_GeomFromText('{}'))".format(code,pt.wkt))
        connection.commit()





#%%

