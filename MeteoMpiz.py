import numpy as np
import simplekml
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


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
        self.Height = np.array(Height)
        self.VelocitySensor_Height = np.array(VelocitySensor_Height)
        self.DirectionSensor_Height = np.array(DirectionSensor_Height)
        self.TemperatureSensor_Height = np.array(TemperatureSensor_Height)
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        if latitude and longitude:
            kml = simplekml.Kml()
            kml.newpoint(name=name, coords=[(latitude, longitude)])
            kml.save(name+'.kml')

    def visual(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1, axisbg='grey')
        rect1 = matplotlib.patches.Rectangle((-2, 0), 4, self.Height, color='black')
        ax1.set_title('Meteorologica Mast')
        ax1.set_xlabel('Ground')
        ax1.set_ylabel('Height[m]')
        ax1.add_patch(rect1)
        for Height in self.VelocitySensor_Height:
            plt.plot((0, 4), (Height, Height), 'k-')
            ax1.text(5, Height,'Velocity sensor at:{0:.2f} m'.format(Height))
        for Height in self.DirectionSensor_Height:
            plt.plot((-4, 0), (Height, Height), 'k-')
            ax1.text(-25, Height, 'Direction sensor at:{0:.2f} m'.format(Height))
        for Height in self.TemperatureSensor_Height:
            plt.plot((-4, 0), (Height, Height), 'k-')
            ax1.text(-25, Height, 'Temperature sensor at:{0:.2f} m'.format(Height))

        plt.xlim([-40, 40])
        plt.ylim([0, self.Height+self.Height/10])
        plt.show()


class ImportedData:

    InputType = 'Name of the Column are defined,if not yes the names with the order should be defined'

    def __init__(self, FilePath, InputType='yes'):
        if InputType=='yes':
            data = pd.read_csv(FilePath, sep='\t', index_col=0, parse_dates=True)
        else:
            ColumnTypes = InputType.split(',')
            data = pd.read_csv(FilePath, sep='\t', names=ColumnTypes, index_col=0, parse_dates=True)
        self.data = data
        self.DataPeriod = pd.date_range(self.data.index[0]._repr_base, self.data.index[-1]._repr_base)
    def SimpleStatistics(self):
        for Name in self.data._info_axis:
            print('----------------', Name,'----------------------------------')
            print('Mean value for ', Name, 'is {0:.2f}'.format(self.data[Name].mean()))
            print('Std value for ', Name, 'is {0:.2f}'.format(self.data[Name].std()))
            print('Max value for ', Name, 'is {0:.2f}'.format(self.data[Name].max()))
            print('Min value for ', Name, 'is {0:.2f}'.format(self.data[Name].min()))

    def filter_Velocity(self, names, MinMaxVelocity = [0,100]):

        for Name in names:
            self.data[Name] =self.data[Name][(self.data[Name] > MinMaxVelocity[0]) & (self.data[Name] < MinMaxVelocity[1])]
            print('Velocity is filter in sensor', Name, 'with Min Velocity ', MinMaxVelocity[0], '[m/s] and Max Velocity', MinMaxVelocity[1], '[m/s]')

    def filter_Direction(self, names, MinMaxDirection=[0,360]):
        for Name in names:
            self.data[Name] =self.data[Name][(self.data[Name] > MinMaxDirection[0]) & (self.data[Name] < MinMaxDirection[1])]
            print('Velocity is filter in sensor', Name, 'with Min Velocity ', MinMaxDirection[0], '[m/s] and Max Velocity', MinMaxDirection[1], '[m/s]')

    def filter_Temperature(self,names, MinMaxTemperature = [-50,100]):

        for Name in names:
            self.data[Name] =self.data[Name][(self.data[Name] > MinMaxTemperature[0]) & (self.data[Name] < MinMaxTemperature[1])]
            print('Velocity is filter in sensor', Name, 'with Min Velocity ', MinMaxTemperature[0], '[m/s] and Max Velocity', MinMaxTemperature[1], '[m/s]')

    def set_Criticalvalues(self):
        print('undone!')

    def plot(self, names):
        plt.style.use('ggplot')
        plt.figure()
        for Name in names:
            self.data[Name].plot(label=Name)
        plt.legend()
        plt.show()

    def MissingValues(self):
        print('not ready yet..')
        self.data['tvalue'] = self.data.index
        self.data['delta'] = (self.data['tvalue']-self.data['tvalue'].shift()).fillna(0)
        DtInSeconds = self.data['delta'].item().total_seconds()
        plt.style.use('ggplot')
        plt.figure()
        DtInSeconds.plot()
        #lol  = self.data.resample('10Min')
        #difft = np.diff()

