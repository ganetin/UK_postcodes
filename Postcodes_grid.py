#------------------------------------#
# import libraries
#------------------------------------#
import postcodes_io_api
import geopandas as gpd
import csv
#------------------------------------#


#------------------------------------#
# Reads the GEOSTAT grid, filters to the UK only, projects the data and obtains the latitude/longitude
#------------------------------------#
grid=gpd.read_file("grid_10km_point.gpkg") # change here the filename for the grid of desired precision
grid_UK=grid[grid["CNTR_ID"]=="UK"]
grid_projected=grid_UK.to_crs(epsg=4326)
grid_projected['lon'] = grid_projected['geometry'].x
grid_projected['lat'] = grid_projected['geometry'].y
#------------------------------------#


#------------------------------------#
# For given latitude and longitude obtains the nearest postcode from postcodes.io and returns a csv file with the format:
# postcode
# latitude
# longitude
#------------------------------------#
pst_obtained=0 # counts the number of postcodes obtained.
api  = postcodes_io_api.Api(debug_http=False)
with open('Postcodes_grid.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Postcode', 'latitude','longitude'])
    postcode=[]
    for index in range(len(grid_projected)):
        lat=grid_projected['lat'].iloc[index]
        lng=grid_projected['lon'].iloc[index]
        data = api.get_nearest_postcodes_for_coordinates(latitude=lat,longitude=lng,limit=1)
        if (data['status']==200):
            if data['result'] is not None:
                pstcd=data['result'][0]['postcode']
                writer.writerow([pstcd,lat,lng])
                pst_obtained=pst_obtained+1
                print('Postcode #',pst_obtained,':',pstcd,'(',lat,lng,')')
        else:
            print('API error')        
print('#------------------#')                
print(pst_obtained,'postcode(s) obtained')                
#------------------------------------#
