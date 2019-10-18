"""Sensor wrapper"""
from camera import Camera
from irproximity_sensor import IRProximitySensor
from ultrasonic import Ultrasonic


class SensorWrapper:
    """The conection to the actual physical sensor, serves as interface to the sensob"""

    def update(self):


    def get_value(self):
        """Gives information to the sensob about this wrapper"""

