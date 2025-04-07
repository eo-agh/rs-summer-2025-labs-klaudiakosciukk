from geoapps.lab03.cloud_mosaic import create_cloud_free_mosaic

import ee
import geemap
ee.Authenticate()
ee.Initialize(project='ee-kkosciukk')

aoi = ee.Geometry.Rectangle([19.8, 50.0, 20.0, 50.2])
mosaic = create_cloud_free_mosaic(aoi, '2023-06-01', '2023-07-01')
print(mosaic.getInfo())

Map = geemap.Map(center=[50.1, 19.9], zoom=10)
Map.addLayer(mosaic, {
    'bands': ['B4', 'B3', 'B2'],
    'min': 0,
    'max': 3000
}, 'Mosaic')
Map