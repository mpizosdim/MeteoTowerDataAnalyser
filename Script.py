#Trial script
# Packages
import simplekml

##
latitude = int(input('Input the latitude of the Meteorological Tower:'))
longitude = int(input('Input the longitude of the Meteorological Tower:'))
NameOfTheAreaTower = input('Name the Area/Meteo Tower:')
kml = simplekml.Kml()
kml.newpoint(name=NameOfTheAreaTower,coords=[(latitude, longitude)])
kml.save('NameOfTheAreaTower'+'.kml')
print(kml)
f = open('winddata.txt','r')
print(f)