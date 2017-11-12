

class Behavior:

    def __init__(self, bbcon, sensob):
        self.bbcon = bbcon
        self.sensob = sensob
        self.motor_recommandations = []
        self.active_flag = False
        self.halt_request = False
        self.priority
        self.match_degree
        self.weight

    def consider_deactivation(self):
        if self.active_flag:
            pass

    def consider_activation(self):
        if not self.active_flag:
            pass

    def update(self):
        pass

    def sense_and_act(self):
        pass

class FollowLine(Behavior):
    pass

class AvoidObstacle(Behavior):
    pass

class CheckDepth(Behavior):
    pass



class CheckColor(Behavior):
    pass




