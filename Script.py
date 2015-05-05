#Trial script
# Packages
import simplekml
import numpy as np
import pandas as pd
import MeteoMpiz
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
    df = pd.read_csv(PathOftheFile, sep='\t', index_col=0, parse_dates=True)
else:
    UserInput = input('Enter the names of the types separated by commas(refer to day if there is)')
    ColumnTypes = UserInput.split(',')
    if ColumnTypes[0]=='date':
        df = pd.read_csv(PathOftheFile, sep='\t', names=ColumnTypes, index_col=0, parse_dates=True)
    else:
        df = pd.read_csv(PathOftheFile, sep='\t', names=ColumnTypes)
print(df)
data = np.array([np.arange(10)]).T
lol = MeteoMpiz.Environment(Pressure=101e3, AirGasConstant=287, AirDensity=[],Temperature=data)
lol.describe()