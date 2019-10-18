"""Class Sensob"""
from sensor_wrapper import SensorWrapper


class Sensob:
    """An interface between sensors and the bbcon´s behaviors"""

    def __init__(self):
        """The main instance variable of a sensob is its associated sensor(s) and its value"""
        sensors = []
        value = ""

    def update(self):
        """Force the sensob to fetch the relevant sensor value(s) and convert to sensob value"""

        # no need to uptade more than once each timestep

        # får info ved å kalle på en wrappers get_value method

