from engine import Engine
from datetime import datetime


class WilloughbyEngine(Engine):

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000