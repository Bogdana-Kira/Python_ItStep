from transport import TransportVehicle

class Plane(TransportVehicle):
    def __init__(self, name, maximum_speed, flight_range):
        super().__init__(name, maximum_speed)
        self.flight_range = flight_range

    def output_information(self):
        print(f"{self.name} з максимальною швидкістю {self.maximum_speed} км/год "
              f"та дальністю польоту {self.flight_range} км")
