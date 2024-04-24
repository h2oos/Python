divisor = 0
dividend = 0
quotient = 0
remainder = 0

print('This program will accept two numbers and divide the first number by the second number')
print('and then display the quotient and the remainder')

dividend = int(input('Please enter first number: '))
divisor = int(input('Please enter second number: '))

if divisor == 0:
    print('Error, cannot divide by 0')

else:
    quotient = dividend // divisor
    remainder = dividend % divisor
    print(f'{dividend} / {divisor} = {quotient} with a remainder of {remainder}')