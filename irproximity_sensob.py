"""A subclass of Sensob"""
from sensob import Sensob
from irproximity_sensor import IRProximitySensor

class IRProximitySensob(Sensob):
    """Calculate the distance to the nearest obstacle by looking at the time differences"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.sensors = [IRProximitySensor()]

    def update(self):
        """Overwrite the update-method in the superclass Sensob"""

