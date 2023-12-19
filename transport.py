class TransportVehicle:
    def __init__ (self, name, maximum_speed):
        self.name = name
        self.maximum_speed = maximum_speed

    def output_information (self):
        print(f"{self.name} з максимальною швидкістю {self.maximum_speed} км/год")
