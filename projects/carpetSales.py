import math
#step 1

# reads input data
inputData=input().split()
# extracts price
pricePerSquare=float(inputData[0])
# width of room
width=int(inputData[1])
# length of the room
length=int(inputData[2])
# area calculation
area=width*length
# calculates cost
cost=area*pricePerSquare
# additional 20% 
cost=cost+cost/5 
print(f'Room: {area} sq ft')
print(f'Carpet: ${cost:.2f}')
 



#step 2

# reads input data
inputData=input().split()
# extracts price
pricePerSquare=float(inputData[0])
# width of room
width=int(inputData[1])
# length of room
length=int(inputData[2])
# calculates area
area=width*length
# calculates cost
carpetCost=area*pricePerSquare
# additional 20% 
carpetCost=carpetCost+carpetCost/5
# calculates labor cost 
laborCost=area*0.75 
print(f'Room: {area} sq ft')
print(f'Carpet: ${carpetCost:.2f}')
print(f'Labor: ${laborCost:.2f}')
 



#step 3

# reads input data
inputData=input().split()
# extracts price
pricePerSquare=float(inputData[0])
# width of room
width=int(inputData[1])
# length of room
length=int(inputData[2])
# calculates area 
area=width*length
# calculates cost
carpetCost=area*pricePerSquare
# additional 20% 
carpetCost=carpetCost+carpetCost/5
# calculates labor cost 
laborCost=area*0.75 
# calculates tax
salesTax=((carpetCost+laborCost)*7)/100
# calculates total cost 
cost=carpetCost+laborCost+salesTax 
print(f'Room: {area} sq ft')
print(f'Carpet: ${carpetCost:.2f}')
print(f'Labor: ${laborCost:.2f}')
print(f'Tax: ${salesTax:.2f}')
print(f'Cost: ${cost:.2f}')
 



#step 4
totalSale=0
orderCount=0
def carpetSale(inputData):
    # extracts price
    pricePerSquare=float(inputData[0])
    # width of room
    width=int(inputData[1])
    # length of room
    length=int(inputData[2])
    # calculates area
    area=width*length
    # calculates cost
    carpetCost=area*pricePerSquare
    # additional 20% 
    carpetCost=carpetCost+carpetCost/5 
    # calculates labor cost
    laborCost=area*0.75 
    # calculates tax
    salesTax=((carpetCost+laborCost)*7)/100 
    # calculates total cost
    cost=carpetCost+laborCost+salesTax 
    global totalSale
    global orderCount
    totalSale=totalSale+cost
    orderCount=orderCount+1
    print("Order #"+str(orderCount))
    print(f'Room: {area} sq ft')
    print(f'Carpet: ${carpetCost:.2f}')
    print(f'Labor: ${laborCost:.2f}')
    print(f'Tax: ${salesTax:.2f}')
    print(f'Cost: ${cost:.2f}')
    print("\n")

# reads input data
inputData1=input().split()
inputData2=input().split()

carpetSale(inputData1)
carpetSale(inputData2)

print(f'Total Sales: ${totalSale:.2f}')

 



#step 5
totalSale=0
orderCount=0
def carpetSale(inputData):
    # extracts price
    pricePerSquare=float(inputData[0])
    #width
    width=int(inputData[1])
    #length
    length=int(inputData[2])
    # calculates area
    area=width*length
    # calculates cost
    carpetCost=area*pricePerSquare
    # additional 20% 
    carpetCost=carpetCost+carpetCost/5 
    # calculates labor cost
    laborCost=area*0.75 
    # calculates tax
    salesTax=((carpetCost+laborCost)*7)/100 
    #calculates total cost    
    cost=carpetCost+laborCost+salesTax 
    global totalSale
    global orderCount
    totalSale=totalSale+cost
    orderCount=orderCount+1
    print("Order #"+str(orderCount))
    print(f'Room: {area} sq ft')
    print(f'Carpet: ${carpetCost:.2f}')
    print(f'Labor: ${laborCost:.2f}')
    print(f'Tax: ${salesTax:.2f}')
    print(f'Cost: ${cost:.2f}')
    print("\n")

# reads input data
inputData1=input().split()
inputData2=input().split()
inputData3=input().split()
carpetSale(inputData1)
carpetSale(inputData2)
carpetSale(inputData3)
print(f'Total Sales: ${totalSale:.2f}')