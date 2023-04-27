class Vehicle:
    def __init__(self, make=None, model=None):
        self.make = make
        self.model = model
        
    def set_vehicle_make(self, make):
        self.make = make
    
    def set_vehicle_model(self, model):
        self.model = model
    
    def get_vehicle_make(self):
        return self.make
    
    def get_vehicle_model(self):
        return self.model


class Car(Vehicle):
    def __init__(self, make=None, model=None, doors=None):
        super().__init__(make, model)
        self.doors = doors
    
    def set_car_door(self, doors):
        self.doors = doors
    
    def get_car_door(self):
        return self.doors


class Truck(Vehicle):
    def __init__(self, make=None, model=None, bed_length=None):
        super().__init__(make, model)
        self.bed_length = bed_length
    
    def set_bed_length(self, length):
        self.bed_length = length
    
    def get_bed_length(self):
        return self.bed_length


def add_car():
    make = input("Please enter the make of the car: ")
    model = input("Please enter the model of the car: ")
    doors = input("Please enter the number of doors: ")
    car = Car(make=make, model=model, doors=doors)
    return car


def add_truck():
    make = input("Please enter the make of the truck: ")
    model = input("Please enter the model of the truck: ")
    bed_length = input("Please enter the bed length of the truck: ")
    truck = Truck(make=make, model=model, bed_length=bed_length)
    return truck


def main():
    vehicles = []
    
    while True:
        print("Welcome to The Johnsons' Car Depot! Let's build your dream vehicle!")
        print("Enter 1 to build a car. Enter 2 to build a truck. Enter 3 to quit.")

        vehicle_type = input("Enter choice: ")
        
        if vehicle_type == "1":
            car = add_car()
            vehicles.append(car)
        elif vehicle_type == "2":
            truck = add_truck()
            vehicles.append(truck)
        elif vehicle_type == "3":
            break
        else:
            print("Bro, you gotta enter 1, 2, or 3")
    
    for vehicle in vehicles:
        if isinstance(vehicle, Car):
            print(f"Car: {vehicle.get_vehicle_make()} {vehicle.get_vehicle_model()}, {vehicle.get_car_door()} doors")
        elif isinstance(vehicle, Truck):
            print(f"Truck: {vehicle.get_vehicle_make()} {vehicle.get_vehicle_model()}, {vehicle.get_bed_length()} bed length")


if __name__ == "__main__":
    main()