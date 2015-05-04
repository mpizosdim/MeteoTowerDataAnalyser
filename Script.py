#Trial script
# Packages
import simplekml
import numpy as np
import pandas as pd
from urllib.request import urlopen

##
latitude = int(input('Input the latitude of the Meteorological Tower:'))
longitude = int(input('Input the longitude of the Meteorological Tower:'))
NameOfTheAreaTower = input('Name the Area/Meteo Tower:')
PathOftheFile = input('Enter the path of the file:')
kml = simplekml.Kml()
kml.newpoint(name=NameOfTheAreaTower, coords=[(latitude, longitude)])
kml.save('NameOfTheAreaTower'+'.kml')


df = pd.read_csv(PathOftheFile, sep='\t')
print(df['date'])
