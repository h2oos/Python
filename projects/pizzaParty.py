import math

# gets user input
x=input().split()
y=input().split()
z=input().split()

# initailizes sum
Sum = 0
total_slices = float(x[0])*float(x[1])
# rounds 
no_pizza = math.ceil(total_slices/8)

# calculates pizza cost
cost_pizza = no_pizza* float(x[2])
# calculates tax
tax_pizza = 0.07 * cost_pizza
temp= 0.2 * cost_pizza
delivery_charge = temp + (0.07*temp)
total_cost = tax_pizza + delivery_charge + cost_pizza
Sum = Sum + total_cost

total_slices1 = float(y[0])*float(y[1])
no_pizza1=math.ceil(total_slices1/8)
cost_pizza1 = no_pizza1 * float(y[2])
tax_pizza1=0.07 * cost_pizza1
temp1=0.2 * cost_pizza1
delivery_charge1 = temp1+(0.07*temp1)
total_cost1 = tax_pizza1 + delivery_charge1 + cost_pizza1
Sum = Sum + total_cost1

total_slices2=float(z[0]) * float(z[1])
no_pizza2 = math.ceil(total_slices2/8)
cost_pizza2 = no_pizza2 * float(z[2])
tax_pizza2=0.07 * cost_pizza2
temp2=0.2 * cost_pizza2
delivery_charge2=temp2 + (0.07 * temp2)
total_cost2 = tax_pizza2 + delivery_charge2 + cost_pizza2
Sum = Sum+ total_cost2

print("\nFriday Night Party")
print(no_pizza,"Pizzas: $",round(cost_pizza,2))
print(f"Tax: ${tax_pizza:.2f}")
print(f"Delivery: ${delivery_charge:.2f}")
print(f"Total: ${total_cost:.2f}")

print("\nSaturday Night Party")
print(no_pizza1,"Pizzas: $",round(cost_pizza1,2))
print(f"Tax: ${tax_pizza1:.2f}")
print(f"Delivery: ${delivery_charge1:.2f}")
print(f"Total: ${total_cost1:.2f}")

print("\nSunday Night Party")
print(no_pizza2,"Pizzas: $",round(cost_pizza2,2))
print(f"Tax: ${tax_pizza2:.2f}")
print(f"Delivery: ${delivery_charge2:.2f}")
print(f"Total: ${total_cost2:.2f}")

print("Weekend Total: $",round(Sum,2))

