string1 = "yes"
string2 = "Yes"
string3 = "no"
string4 = "No"
while True:
    string = str(input("Do you want to proceed: "))
    if string == string1 or string ==  string2:
       binary_number = int(input("Enter a Binary Number: "))
       decimal_value=0
       i = 1
       length = len(str(binary_number))

       for k in range(length):
          reminder = binary_number % 10
          decimal_value = decimal_value + (reminder * i)
          i = i * 2
          binary_number = int(binary_number/10)

       print("Decimal number is  ", decimal_value)
       
    elif string == string3 or string == string4 :
        print ("Exit")
        break
   
    else:
       print('Please try again, wrong input')