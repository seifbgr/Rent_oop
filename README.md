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
# Setup
v1 = Vehicle("AB-123-CD", "Toyota", "SUV")
cust = Customer("Alice", 30, "C001")
emp = Employee("Tom", 45, "E001", "Downtown")

# Assign vehicle
emp.assign_vehicle(v1, cust)

# View rentals
cust.view_rentals()

# Return vehicle
cust.return_vehicle(v1)
