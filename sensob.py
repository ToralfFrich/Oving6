class Sensob():

    # initializes sensors in an array

    def __init__(self, sensors):
        self.sensors = sensors


    def getValue(self,sensor):
        return sensor.getValue()

    def update(self):
        values = []
        for sensor in self.sensors:
            value = self.sensor.getValue()
            values.append(value)
        return values

