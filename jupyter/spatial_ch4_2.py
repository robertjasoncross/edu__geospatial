#%%

import os
import rasterio

dataset = rasterio.open(r"data/Natural_Earth_quick_start/50m_raster/NE1_50M_SR_W/NE1_50M_SR_W.tif") 
dataset.count
dataset.width
dataset.height
dataset.bounds
dataset.crs

#%%

band1 = dataset.read(1)
band1

#%%

%matplotlib inline
from matplotlib import pyplot
pyplot.imshow(dataset.read(1))
pyplot.show()

#%%

!gdalinfo --formats


#%%
