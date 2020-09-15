# About
Obtain and visualize a list of postcodes for the whole UK.

* Postcodes_grid.py: obtains a list (in csv format) of postcodes covering the whole UK based on a EUROSTAT grid of given precision. The better the precision the larger the number of postcodes.
* Postcodes_map.ipynb: shows a map of the obtained postcodes vs. the EUROSTAT grid

## Prerequisites:
Postcodes_grid.py:
* [geopandas] (https://geopandas.org/)
* [Python csv module] (https://docs.python.org/3/library/csv.html)
* Python Wrapper for [postcodes.io API] (https://pypi.org/project/postcodes-io-api/) - no key needed
* a GEOSTAT grid of chosen resolution: download [here] (https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/grids) ***in geometry type: point***

Postcodes_map.ipynb:
* [pandas] (https://pandas.pydata.org/)
* [geopandas] (https://geopandas.org/)
* [folium] (https://python-visualization.github.io/folium/)


## Output
A csv file containing the postcodes of the grid points and the latitude and longitude of these points

## Example
Results obtained with a 10x10 km^2 grid are given here as an example.
* Output in Postcodes_grid.csv
* Notebook available [here] (https://nbviewer.jupyter.org/github/ganetin/UK_postcodes/blob/master/Postcodes_map.ipynb) and map [here] (Postcodes_map.html)

## License
MIT License

## Author
Dr. Morgane FORTIN, Sept. 2020
