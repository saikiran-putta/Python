foods = []
prices = []
total = 0
while True:
    food = input("Enter the food you wanna buy(q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of {food}: Rs."))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")
for food, price in zip(foods, prices):
    print(f"{food} : Rs.{price}/-")

for price in prices:
    total += price



print(f"Your total bill is Rs.{total}/-")

