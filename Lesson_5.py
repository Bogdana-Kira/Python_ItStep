class TransportVehicle:
    def __init__(self, name, maximum_speed):
        self.name = name
        self.maximum_speed = maximum_speed

    def output_information(self):
        print(f"{self.name} з максимальною швидкістю {self.maximum_speed} км/год")

Transport1 = TransportVehicle("Автомобіль", 200)
Transport1.output_information()

class Plane(TransportVehicle):
    def __init__(self, name, maximum_speed, flight_range):
        super().__init__(name, maximum_speed)
        self.flight_range = flight_range

    def output_information(self):
        print(f"{self.name} з максимальною швидкістю {self.maximum_speed} км/год "
              f"та дальністю польоту {self.flight_range} км")

Plane1 = Plane("Боїнг 747", 900, 12000)
Plane1.output_information()

from airplane import Plane

attributes_methods = dir(Plane)
print(attributes_methods)

