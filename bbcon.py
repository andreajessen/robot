"""Higest-level class - require one instance"""
from arbitrator import Arbitrator
from behavior import *
from camera_sensob import CameraSensob
from irproximity_sensob import IRProximitySensob
from reflectance_sensob import ReflectanceSensob
from ultrasonic import Ultrasonic
from zumo_button import ZumoButton


class BBCON:
    """class BBCON"""

    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = Arbitrator()
        self.behavior_values = {'motor_duration': 0.5, 'min_distance': 5.0,
                                'goPri': 1,'backwards': [-1, -1], "forward": [1, 1], 'whitePri': 2,
                                'white_scale': 0.9, 'turn': [1, 0], 'cameraPri': 5, 'stop': [0, 0],
                                "red_scale": 0.95, 'collitionPri': 4}

    def add_behavior(self, behavior):
        """legg til ny behavior"""
        if behavior not in self.behaviors:
            self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        """legg til en ny sensob"""
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)

    def activate_behavior(self, behavior):
        """legg til en eksisterende behavoir i active-behavior"""
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        """fjern en eksisterende behavoir i active_behavior"""
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)

    def run_one_timestep(self):
        """hoved BBCON activity"""
        for sensob in self.sensobs:
            sensob.update()

        for behavior in self.behaviors:
            behavior.update()
            if behavior.activate_flag:
                self.activate_behavior(behavior)
            else:
                self.deactivate_behavior(behavior)
        recommentations, stop = self.arbitrator.choose_action(self.active_behaviors)
        for i in range(len(self.motobs)):
            self.motobs[i].update(recommentations[i])

        for sensob in self.sensobs:
            sensob.reset()

    def main(self):
        ultra_sonic = Ultrasonic()
        ir_sensor = ReflectanceSensob()
        camera = CameraSensob()
        go = Go(self)
        collide = AvoidCollision(self, ultra_sonic)
        white = AvoidWhiteline(self, ir_sensor)
        stop = Stop(self, camera)
        self.sensobs.append(ultra_sonic)
        self.sensobs.append(ir_sensor)
        self.sensobs.append(camera)
        self.behaviors.append(go)
        self.behaviors.append(collide)
        self.behaviors.append(white)
        self.behaviors.append(stop)
        zumo = ZumoButton()
        zumo.wait_for_press()
        while True:
            self.run_one_timestep()
            print("RUN")


if __name__ == "__main__":
    bbcon = BBCON()
    bbcon.main()




