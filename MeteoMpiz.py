import numpy as np
class Environment:
    def __init__(self, Pressure=[],AirGasConstant=[], AirDensity=[],Temperature=[]):
        KelvinConstant = 273.15
        Pressure,AirGasConstant,AirDensity,Temperature = np.asarray([
            Pressure,AirGasConstant,AirDensity,Temperature])
        if (not Pressure) and (AirGasConstant) and (AirDensity) and (AverageTemp):
            print('Calculating Pressure...')
        if (Pressure) and (not AirGasConstant) and (AirDensity) and (AverageTemp):
            print('Calculating Air Gas Constant...')
        if not (Pressure) and (AirGasConstant) and (not AirDensity) and (AverageTemp):
            print('Calculating Air Density...')
            AirDensity = Pressure/(AirGasConstant*(Temperature+KelvinConstant))
        if not (Pressure) and (AirGasConstant) and (not AirDensity) and (AverageTemp):
            print('Calculating temperature...')
