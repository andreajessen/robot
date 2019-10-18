"""A subclass of Sensob"""
from sensob import Sensob
from ultrasonic import Ultrasonic
from irproximity_sensor import IRProximitySensor


class Distance(Sensob):
    """Calculate the distance to the nearest obstacle by looking at the time differences"""

    def __init__(self, sensors):
        """Initialize"""
        super().__init__()

