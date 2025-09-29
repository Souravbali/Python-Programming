# Q4. E-Commerce Discount Calculator
# Write a program that asks for product price and user type (Regular, Premium, VIP).
# Discount Rules:
# •	Regular:
# o	< 500 → 5%
# o	≥ 500 → 10%
# •	Premium:
# o	< 1000 → 15%
# o	≥ 1000 → 20%
# •	VIP: Flat 25% discount always
# Also apply extra 5% discount if payment mode = "Online".
# Finally display the discounted price.

product_price = int(input("Enter the product price:"))
user_type = input("Enter the user type:")
if user_type == "Regular":
   if product_price<500:
      discount = (5/100)*product_price
   else:
         discount = (10/100)*product_price

elif user_type == "Premium":
   if product_price<1000:
      discount = (15/100)*product_price
   else:
      discount = (20/100)*product_price

elif user_type == "VIP":
   discount = (25/100)*product_price

else:
   print("Enter the invalid input")

if user_type in ["Regular", "Premium", "VIP"]:
    online = input("Do you want to pay online:")
    if online == 'yes':
        extra_discount = (5/100)*product_price
        discounted_price = product_price - (discount + extra_discount)  
        print(f"Final price after discounts: {discounted_price}")
    else:
        final_price = product_price - discount  
        print(f"Discount amount: {discount}")
        print(f"Final price when paying offline: {final_price}")