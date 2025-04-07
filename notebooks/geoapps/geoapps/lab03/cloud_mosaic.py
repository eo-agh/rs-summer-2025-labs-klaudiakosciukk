import ee

def mask_clouds(image):
    qa = image.select('QA60')
    cloud_bit_mask = 1 << 10
    cirrus_bit_mask = 1 << 11
    mask = qa.bitwiseAnd(cloud_bit_mask).eq(0).And(
           qa.bitwiseAnd(cirrus_bit_mask).eq(0))
    return image.updateMask(mask).copyProperties(image, image.propertyNames())

def create_cloud_free_mosaic(aoi, start_date, end_date):
    collection = (ee.ImageCollection("COPERNICUS/S2")
                    .filterBounds(aoi)
                    .filterDate(start_date, end_date)
                    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 60))
                    .map(mask_clouds))
    mosaic = collection.median().clip(aoi)
    return mosaic
