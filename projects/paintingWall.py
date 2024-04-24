from math import ceil   

# height of wall
height = float(input()) #
# width of wall
width = float(input())  
# input cost of 1 paint can
cost_of_1_paint = float(input())   

# calculates wall area 
wall_area = height * width  

# prints wall area
print(f"Wall area: {wall_area:.1f} sq ft")

# calculate gallons of paint needed
paint_needed = wall_area / 350.0 

# print number of gallons of paint
print(f"Paint needed: {paint_needed:.3f} gallons")

# calculates total paint cans needed
cans_needed = ceil(paint_needed)

# prints total cans needed
print(f"Cans needed: {cans_needed} can(s)")


# calculates paint cost
paint_cost = cost_of_1_paint * cans_needed

# prints paint cost
print(f"Paint cost: ${paint_cost:.2f}")

# calculates sales tax of 7 %
sales_tax = paint_cost * 0.07

# prints sales tax
print(f"Sales tax: ${sales_tax:.2f}")

# calculates total cost 
total_cost = paint_cost + sales_tax

# print total cost
print(f"Total cost: ${total_cost:.2f}")
