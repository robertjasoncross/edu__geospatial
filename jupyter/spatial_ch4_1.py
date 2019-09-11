#%%

import geopandas as gp
import os

path = os.getcwd()
print(path)


#%%

df = gp.read_file(r'data/Natural_Earth_quick_start/10m_cultural/ne_10m_admin_0_boundary_lines_land.shp')
df.head()

# merc= df.to_crs({'init': 'epsg:3395'})
# merc.plot(color='black')

#%%
#import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
%matplotlib inline

# fig, ax = plt.subplots(facecolor='lightslategray')
figure(figsize=(10,10))
ax = df.plot(color='black', edgecolor='white')
ax.set_facecolor("white")

#%%

df.geom_type.head()
df.crs

j = df.to_json
print(j)

#%%