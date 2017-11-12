from motors import *


class Motob:

    def __init__(self):
        self.value = (None, None)
        self.motor = Motors()


    def update(self, recommendation):
        self.value = recommendation


    def operationalize(self):

        self.motor.set_value(self.value, 0.5)


def main():
    motor = Motob()

    motor.update((1,1))
    motor.operationalize()






