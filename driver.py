"""from driver import Driver"""

class Driver:
    """Driver class."""
    def __init__(self,
                name: str,
                rating: float = None,
                car_make: str = None,
                car_model: str = None,
                age: int = None,
                passengers: list = None):
        self.name = name
        self.rating = rating
        self.car_make = car_make
        self.car_model = car_model
        self.age = age
        self.passengers = passengers

    def passenger_names(self):
        return [passenger.name for passenger in self.passengers]
