# Q6. Movie Ticket Pricing System
# Inputs: age, movie_type (2D/3D), day (weekday/weekend).
# Rules:
# •	Base price = ₹200
# •	If 3D → +₹100
# •	Weekend → +₹50
# •	Age < 12 → 50% discount
# •	Age > 60 → 30% discount
# Calculate and display final ticket price.
age = int(input("Enter the age: "))
movie_type = input("Enter the movie type: ")
day = input("Enter the day: ")
base_price = 200

if movie_type == "3D" or movie_type == "3d":
    base_price += 100

if day == "Weekend" or day == "weekend"or day=="sunday" or day == "saturday":
    base_price += 50

if age < 12:
    base_price = base_price-(0.5*base_price)
elif age > 60:
    base_price = base_price-(0.3*base_price)  


print("Final price:", base_price)