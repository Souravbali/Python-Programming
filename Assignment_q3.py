# Q3. Smart Traffic Fine System
# A city wants to implement a traffic fine system.
# Inputs: speed, vehicle_type (car/bike/truck), seat_belt (Yes/No), helmet (Yes/No if bike).
# Rules:
# •	Speed > 80 → Fine ₹2000
# •	Car without seat belt → +₹1000 fine
# •	Bike without helmet → +₹1500 fine
# •	Truck speed > 60 → +₹3000 fine
# Display: "Total Fine = …"
# If no rules violated → "No Fine. Drive Safe 
speed = int(input("Enter the speed: "))
vehicle_type = input("Car/bike/truck: ")
seat_belt = input("Seat belt: yes/no-> ")
helmet = input("Helmet: yes/no-> ")
fine = 0


if vehicle_type == 'car':
    if seat_belt == 'no': 
        fine += 1000
    if speed > 80: 
        fine += 2000
        
elif vehicle_type == 'bike':
    if helmet == 'no': 
        fine += 1500
    if speed > 80:
        fine += 2000
        
elif vehicle_type == 'truck':
    if seat_belt == 'no':
        fine += 1000
    if speed > 60:
        fine += 3000
        
else:
    print("Invalid vehicle type")

if fine == 0 and vehicle_type in ['car', 'bike', 'truck']:
    print("No fine, safe driving!")
else:
    print("Total fine:", fine)