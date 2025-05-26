class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Customer(Person):
    def __init__(self, name, age, customer_id, rented_vehicles=None):
        super().__init__(name, age)
        self.customer_id = customer_id
        self.rented_vehicles = rented_vehicles if rented_vehicles is not None else []

    def rent_vehicle(self, vehicle):
        if not vehicle.is_rented and len(self.rented_vehicles) < 2:
            self.rented_vehicles.append(vehicle)
            vehicle.rent_out()
            print(f"The vehicle {vehicle.plate_number} has been rented!")
        elif vehicle.is_rented:
            print(f" The vehicle {vehicle.plate_number} is already rented.")
        else:
            print(f" {self.name} cannot rent more than 2 vehicles.")

    def return_vehicle(self, vehicle):
        if vehicle in self.rented_vehicles:
            self.rented_vehicles.remove(vehicle)
            vehicle.return_back()
            print(f"{self.name} has returned vehicle {vehicle.plate_number}.")
        else:
            print(f"{self.name} has not rented vehicle {vehicle.plate_number}.")

    def view_rentals(self):
        if not self.rented_vehicles:
            print(f"There are no rented vehicles for {self.name}.")
        else:
            print(f"Rented vehicles for {self.name}:")
            for vehicle in self.rented_vehicles:
                print(f" - {vehicle.plate_number}: {vehicle.type} from {vehicle.brand}")


class Employee(Person):
    def __init__(self, name, age, employee_id, assigned_location):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.assigned_location = assigned_location
        self.assigned_customers = []

    def assign_vehicle(self, vehicle, customer):
        if vehicle.is_rented:
            print(f" Vehicle {vehicle.plate_number} is already rented.")
        elif len(customer.rented_vehicles) >= 2:
            print(f" {customer.name} cannot rent more than 2 vehicles.")
        else:
            self.assigned_customers.append(customer)
            customer.rent_vehicle(vehicle)


class Vehicle:
    def __init__(self, plate_number, brand, type_, is_rented=False):
        self.plate_number = plate_number
        self.brand = brand
        self.type = type_
        self.is_rented = is_rented

    def rent_out(self):
        if self.is_rented:
            print(f" The vehicle {self.plate_number} is already rented.")
        else:
            self.is_rented = True
            print(f" The vehicle {self.plate_number} is now rented.")

    def return_back(self):
        if not self.is_rented:
            print(f" The vehicle {self.plate_number} is already available.")
        else:
            self.is_rented = False
            print(f" The vehicle {self.plate_number} has been returned.")

    def show_status(self):
        print(f" Plate Number: {self.plate_number}")
        print(f" Brand: {self.brand}")
        print(f" Type: {self.type}")
        print(f" Status: {'Rented' if self.is_rented else 'Available'}")




vh1 = Vehicle("A018973","Peugeout",'Car')
vh2 = Vehicle("A018972","Renault",'trak')
vh3 = Vehicle("A018976","Fiat",'Car')
vh4 = Vehicle("A018979","Opel",'Car')

cst1 = Customer('Seif',34,"A018")
cst2 = Customer('Ali',30,"A019")
cst3 = Customer('Jaen',32,"A011")

Emp = Employee('Alex', 22,"A0190","France")

Emp.assign_vehicle(vh1,cst2)
Emp.assign_vehicle(vh2,cst2)
Emp.assign_vehicle(vh3,cst2)
Emp.assign_vehicle(vh3,cst1)

vh1.show_status()
cst2.view_rentals()
cst1.view_rentals()
cst3.view_rentals()




