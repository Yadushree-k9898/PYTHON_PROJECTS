foods = []
prices = []
total = 0

while True:
    food = input('Enter a food to buy (q to quit): ')
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'Enter the price of {food}: INR '))
        foods.append(food)
        prices.append(price)


print("-----------YOUR CART-------------")

for food in foods:
    print(foods, end=" ")
    
for price in prices:
    total = total + price
    
    
print()
print(f'Your total is : INR {total}')