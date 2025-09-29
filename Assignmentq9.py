# Q9. Online Food Delivery Charges
# Inputs: distance, order_amount, user_type (Normal, Gold, Platinum).
# Rules:
# •	Base delivery = ₹50
# •	If distance > 5 km → +₹10/km extra
# •	Free delivery if order_amount ≥ 1000
# •	Membership benefits:
# o	Gold → 20% discount on order
# o	Platinum → 30% discount on order
# o	Normal → No discount
distance = int(input("Enter the distance: "))
order_amount = int(input("Enter the order amount: "))
User_type = input("Normal,Gold,Platinum: ")
base_delievery = 50
if distance>5:
    base_delievery = base_delievery+10*(distance-5)
if order_amount >=1000:
    base_delievery = 0

if User_type == "Gold":
    order_amount = (order_amount+base_delievery) - (order_amount+base_delievery)*0.2

if User_type == "Platinum":
    order_amount = (order_amount+base_delievery)-(order_amount+base_delievery)*0.3
if User_type == "Normal":
   order_amount = order_amount +  base_delievery
    

print("Overall bill:",order_amount)