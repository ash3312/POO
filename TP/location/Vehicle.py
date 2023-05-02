from datetime import datetime

class Vehicle:
    def __init__(self, id, make, model, year, daily_rate) -> None:
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.rented = False

    def __str__(self) -> str:
        return f" {self.id} : {self.make} {self.model} {self.year} ({self.daily_rate} $/jour)"


class Car(Vehicle):
    def __init__(self, id, make, model, year, daily_rate, num_doors, top_speed) -> None:
        super().__init__(id, make, model, year, daily_rate)
        self.num_doors = num_doors
        self.top_speed = top_speed

    def __str__(self) -> str:
        return "Voiture" + super().__str__()

class Truck(Vehicle):
    def __init__(self, id, make, model, year, daily_rate, payload_capacity, num_axles) -> None:
        super().__init__(id, make, model, year, daily_rate)
        self.payload_capacity = payload_capacity
        self.num_axles = num_axles
    
    def __str__(self) -> str:
        return "Camion" + super().__str__()

class RentalAgreement:
    def __init__(self, vehicle, start_date, end_date) -> None:
        self.vehicle = vehicle
        self.start_date = datetime.strptime(start_date, "%d-%m-%Y")
        self.end_date = datetime.strptime(end_date, "%d-%m-%Y")
        

    def total_cost(self):
      return ((self.end_date - self.start_date ).days +1) * self.vehicle.daily_rate
    
    def __str__(self) -> str:
        return f"RentalAgreement : {self.vehicle} {self.start_date.date()} {self.end_date.date()} ({self.total_cost()} $)"

class RentalSystem:
    def __init__(self) -> None:
        self.vehicles = []
        self.agreements = []

    def add_vehicle(self, vehcile):
        self.vehicles.append(vehcile)

    def remove_vehicle(self, vehicle):
        for i in range(len(self.vehicles)):
            if self.vehicles[i] == vehicle:
                del self.vehicles[i]
                return

    def list_vehicles(self):
        for v in self.vehicles:
            print(v, "\t")

    def create_agreement(self, agreement):
        if agreement.vehicle.rented:
            raise ValueError("This is already rented")
        agreement.vehicle.rented = True
        self.agreements.append(agreement)
    
    def list_agreement(self):
        for a in self.agreements:
            print(a, "\t")

    def return_vehicle(self, vehicle):
        for i in range(len(self.vehicles)):
            if self.vehicles[i] == vehicle:
                self.vehicles[i].rented = False
                return
            
rental_system = RentalSystem()

car1 = Car("1", "BMW", "E6", "2020", 30, 4, 220)
car2 = Car("2", "BMW", "E7", "2021", 45, 4, 220)
print(car1)

rental_system.add_vehicle(car1)
rental_system.add_vehicle(car2)

agreement = RentalAgreement(car1, "01-05-2023", "10-05-2023")
print(agreement.total_cost())

rental_system.create_agreement(agreement)
rental_system.return_vehicle(car1)
agreement = RentalAgreement(car1, "01-06-2023", "10-06-2023")
rental_system.create_agreement(agreement)


rental_system.list_agreement()
rental_system.list_vehicles()

