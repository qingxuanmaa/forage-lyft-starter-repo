from serviceable import Serviceable

class Car:
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires
        
    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service() or self.tires.needs_service()