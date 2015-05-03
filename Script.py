#Trial script
# Packages
import simplekml
import csv
##
latitude = int(input('Input the latitude of the Meteorological Tower:'))
longitude = int(input('Input the longitude of the Meteorological Tower:'))
NameOfTheAreaTower = input('Name the Area/Meteo Tower:')
PathOftheFile = input('Enter the path of the file:')
kml = simplekml.Kml()
kml.newpoint(name=NameOfTheAreaTower, coords=[(latitude, longitude)])
kml.save('NameOfTheAreaTower'+'.kml')





