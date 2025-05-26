# 🚗 Vehicle Rental System

This is a simple Object-Oriented Python project simulating a vehicle rental system. It models customers, employees, and vehicles, and allows basic rental operations such as assigning, returning, and tracking rented vehicles.

---

## 🧱 Features

- Add customers and employees.
- Assign vehicles to customers if available.
- Enforce rules like maximum 2 rentals per customer.
- Return vehicles and update availability status.
- View current rentals for each customer.
- Track vehicle rental status.

---

## 🏗️ Classes Overview

### `Person`
Base class for shared attributes:
- `name`
- `age`

### `Customer(Person)`
Represents a client:
- `customer_id`
- `rented_vehicles`: list of rented vehicles

**Methods:**
- `rent_vehicle(vehicle)`
- `return_vehicle(vehicle)`
- `view_rentals()`

### `Employee(Person)`
Represents a rental agent:
- `employee_id`
- `assigned_location`

**Methods:**
- `assign_vehicle(vehicle, customer)`

### `Vehicle`
Represents a vehicle:
- `plate_number`
- `brand`
- `type`
- `is_rented`

**Methods:**
- `rent_out()`
- `return_back()`
- `show_status()`

---

## ✅ Sample Use

```python
# Create a vehicules
vh1 = Vehicle("A018973","Peugeout",'Car')
vh2 = Vehicle("A018972","Renault",'trak')
vh3 = Vehicle("A018976","Fiat",'Car')
vh4 = Vehicle("A018979","Opel",'Car')

# Create a Customers


cst1 = Customer('Seif',34,"A018")
cst2 = Customer('Ali',30,"A019")
cst3 = Customer('Jaen',32,"A011")

#Effect Custumers to there Vehicules

Emp = Employee('Alex', 22,"A0190","France")

Emp.assign_vehicle(vh1,cst2)
Emp.assign_vehicle(vh2,cst2)
Emp.assign_vehicle(vh3,cst2)
Emp.assign_vehicle(vh3,cst1)

# Show a results

vh1.show_status()
cst2.view_rentals()
cst1.view_rentals()
cst3.view_rentals()

