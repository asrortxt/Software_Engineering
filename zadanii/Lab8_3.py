from Lab8_2 import Car
class ElectroCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make,model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electronic_car = ElectroCar("Tesla", "Model S", 75)
my_electronic_car.drive()
my_electronic_car.charge()