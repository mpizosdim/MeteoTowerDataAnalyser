#Trial script
import numpy as np
import MeteoMpiz

data = np.array([np.arange(10)]).T
lol = MeteoMpiz.Envisronment(Pressure=101e3, AirGasConstant=287, AirDensity=[],Temperature=data)
lol2 = MeteoMpiz.MeteoMast(90, VelocitySensor_Height=[20,10], DirectionSensor_Height=[10,20,30], TemperatureSensor_Height=[40], name='Meteorological Mast')
lol3 = MeteoMpiz.ImportedData('winddata.txt')
lol3.SimpleStatistics()
