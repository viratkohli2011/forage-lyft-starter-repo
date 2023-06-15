from engine import Engine
from datetime import datetime


class CapuletEngine(Engine):

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
