"""Motbo klassen"""


class Motob:

    def __init__(self, motors, bbcon):
        self.motors = motors
        self.values = []
        self.bbcon = bbcon

    def update(self, values):
        """Motta en ny motor recommendation, load it into the value slot and operationalize"""
        self.values = values
        print("Motob value: ", self.values)
        self.operationalize()

    def operationalize(self):
        """konverter en motor recommendation til en eller fler motor motor settings, som sendes til riktig motor"""
        self.motors.set_value(self.values, self.bbcon.behavior_values['motor_duration'])
