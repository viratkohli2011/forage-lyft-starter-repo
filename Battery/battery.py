from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery
from car import Car

class Battery(Car):

    def needs_service(self):
        return SpindlerBattery.needs_service() or NubbinBattery.needs_service():
