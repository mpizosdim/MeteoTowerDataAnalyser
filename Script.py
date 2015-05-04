#Trial script
# Packages
import simplekml
import numpy as np
import pandas as pd

##
##latitude = int(input('Input the latitude of the Meteorological Tower:'))
##longitude = int(input('Input the longitude of the Meteorological Tower:'))
##NameOfTheAreaTower = input('Name the Area/Meteo Tower:')
PathOftheFile = input('Enter the path of the file:')
##kml = simplekml.Kml()
##kml.newpoint(name=NameOfTheAreaTower, coords=[(latitude, longitude)])
##kml.save('NameOfTheAreaTower'+'.kml')

TypeOfInput = input('Are the name/type of the columns defined in the file?')

if TypeOfInput=='yes':
    df = pd.read_csv(PathOftheFile, sep='\t')
else:
    UserInput = input('Enter the names of the types separated by commas')
    ColumnTypes = UserInput.split(',')
    df = pd.read_csv(PathOftheFile, sep='\t', names=ColumnTypes)
print(df)
