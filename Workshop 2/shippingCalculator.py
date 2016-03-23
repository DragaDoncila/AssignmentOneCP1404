"""This program calculates total shipping charge for a number of items"""
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1

num_items = int(input("Please enter a number of items: "))
while num_items <= 0:
    print("Invalid number of items!")
    num_items = int(input("Please enter a number of items: "))

total_cost = 0
for i in range(1, num_items + 1):
    cost_shipping_per_item = float(input("What is the cost of shipping item {}? $".format(i)))
    total_cost += cost_shipping_per_item

if total_cost >= DISCOUNT_THRESHOLD:
    discount = total_cost * DISCOUNT_RATE
    total_cost -= discount

print("Total cost is ${:^10,.2f}".format(total_cost))
