from capulet_engine import CapuletEngine
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine
from car import Car


class Engine(Car):

    def needs_service(self):
        return CapuletEngine.needs_service() or SternmanEngine.needs_service() or WilloughbyEngine.needs_service():
