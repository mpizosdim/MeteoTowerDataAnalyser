import numpy as np


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