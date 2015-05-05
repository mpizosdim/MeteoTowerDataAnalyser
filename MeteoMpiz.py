import numpy as np
import simplekml

class Environment:
    Pressure = 'atmospheric pressure'
    AirGasConstant = 'Gas constant for air'
    AirDensity = 'Air Density'

    def __init__(self, Pressure=[],AirGasConstant=[], AirDensity=[],Temperature=[]):
        KelvinConstant = 273.15
        if (not Pressure) and (AirGasConstant) and (AirDensity) and (Temperature.size):
            print('Calculating Pressure...')
            Pressure = AirGasConstant*(AirDensity*(Temperature+KelvinConstant))
        if (Pressure) and (not AirGasConstant) and (AirDensity) and (Temperature.size):
            print('Calculating Air Gas Constant...')
            AirGasConstant = Pressure/(AirDensity*(Temperature+KelvinConstant))
        if (Pressure) and (AirGasConstant) and (not AirDensity) and (Temperature.size):
            print('Calculating Air Density...')
            AirDensity = Pressure/(AirGasConstant*(Temperature+KelvinConstant))
        else:
            print('Some values are missing.Furthermore Temperature is essential...')

        self.Pressure = Pressure
        self.AirGasConstant = AirGasConstant
        self.AirDensity = AirDensity

    def describe(self):
        print('Mean value of Air Density is {0:.2f}'.format(self.AirDensity.mean()))
        print('Gas constant of Air is %d'%self.AirGasConstant)
        print('Pressure is %d'%self.Pressure)


class MeteoMast:
    Height = 'Height of the Meteorological Mast'
    VelocitySensor_Height = 'Vector with the heights of the Sensors for the Velocity'
    DirectionSensor_Height = 'Vector with the heights of the Sensors for the Direction'
    TemperatureSensor_Height = 'Vector with the heights of the Sensors for the Temperature'

    def __init__(self, Height, VelocitySensor_Height, DirectionSensor_Height, TemperatureSensor_Height, name='Meteorological Mast', latitude=[], longitude=[]):
        self.Height = Height
        self.VelocitySensor_Height = VelocitySensor_Height
        self.DirectionSensor_Height = DirectionSensor_Height
        self.TemperatureSensor_Height = TemperatureSensor_Height
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        if (latitude) and (longitude):
            kml = simplekml.Kml()
            kml.newpoint(name=name, coords=[(latitude, longitude)])
            kml.save(name+'.kml')

