def minandmax(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    for i in numbers:
        if int(i) < int(minimum):
            minimum = i
        if int(i) > int(maximum):
            maximum = i
    
  
    print('The minimum is', minimum)
    print('The maximum is', maximum)

def mean(numbers):

    sum = 0
    for i in numbers:
        sum = sum + int(i)
    mean = sum / len(numbers)
   
    print(f'The mean is {mean:.1f}')

def palindrome(numbers):

    palindrome = True
    for i in range(len(numbers)):
        if numbers[i] != numbers[len(numbers) - i - 1]:
            palindrome = False
            break
    if palindrome:
        palindrome = 'true'
    else:
        palindrome = 'false'
    # print palindrome
    print('The list is palindrome:', palindrome)

def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        median = (int(numbers[len(numbers) // 2]) + int(numbers[len(numbers) // 2 - 1])) / 2
    else:
        median = numbers[len(numbers) // 2]

    print('The median is', median)

def mode(numbers):
    mode = numbers[0]
    count = 1
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            count += 1
            if count > 1:
                mode = numbers[i]
        else:
            count = 1
  
    print('The mode is', mode)

def ascend(numbers):
    print('Sorted list:', numbers)
    

def main():
 
    numbers = input('Enter a list of numbers, separated by commas: ')

    numbers = numbers.split(',')
    minandmax(numbers)
    mean(numbers)
    palindrome(numbers)
    median(numbers)
    mode(numbers)
    ascend(numbers)

if __name__ == "__main__":
    main()
