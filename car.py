from abc import ABC
from car_factory import CarFactory
from engine import Engine
from battery import Battery
from serviceable import Serviceable

class Car(ABC, CarFactory, Engine, Battery, Serviceable):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def __engine(self):
        pass

    def __battery(self):
        pass

    def needs_service(self):
        return Engine.needs_service() or Battery.needs_service()
