from ultrasonic import Ultrasonic
from reflectance_sensors import ReflectanceSensors
import sensob
import bbcon

class Behavior:

    def __init__(self, bbcon, sensob):
        self.bbcon = bbcon
        self.sensob = sensob
        self.motor_recommandations = (0,0)
        self.active_flag = False
        self.halt_request = False
        self.priority
        self.match_degree
        self.weight

    def consider_deactivation(self):
        return False

    def consider_activation(self):
        return False

    def update(self):
        return False

    def sense_and_act(self):
        return False

class FollowLine(Behavior):

    def __init__(self, bbcon, sensob):
        super().__init__(bbcon, sensob)


    def consider_activation(self):
        if self.sensob.update()[0] > 10 and min(self.sensob.update()[1]) < 0.5:
            self.active_flag = True

    def consider_deactivation(self):
        if self.sensob.update()[0] < 10:
            self.active_flag = False

    def sense_and_act(self):
        values = self.sensob.update()[1]
        if ((values[0] + values[1])/2) < ((values[3]+values[4])/2):
            self.motor_recommandations = (0.3, 0.5)
        elif ((values[0] + values[1])/2) > ((values[3]+values[4])/2):
            self.motor_recommandations = (0.5,0.3)
        else:
            self.motor_recommandations = (0.5,0.5)




class AvoidObstacle(Behavior):
    pass

class CheckDepth(Behavior):

    def __init__(self, bbcon, sensob):
        super().__init__(bbcon, sensob)

    def consider_activation(self):
        if self.sensob.update()[0] > 10:
            self.active_flag = True

    def consider_deactivation(self):
        if self.sensob.update()[0] < 10:
            self.active_flag = False

    def update(self):
        self.consider_activation()
        if not self.active_flag:
            self.match_degree = 0
            return
        #Kjører hvis active flag == True
        self.sense_and_act()
        self.weight = self.priority * self.match_degree
        self.consider_deactivation()

    def sense_and_act(self):
        self.motor_recommandations = (0,0)
        self.priority = 0.9
        self.match_degree = 0.9



class CheckColor(Behavior):
    pass




