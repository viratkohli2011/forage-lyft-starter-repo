from car import Car
from abc import ABC


class Serviceable(Car, ABC):

    def needs_service(self):
        return Car.needs_service()