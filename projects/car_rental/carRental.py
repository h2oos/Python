carType = str(input('Please enter car type (luxury, midsize, or compact): '))
rentalDay = int(input('Please enter rental day: '))
rentalWeek = int(input('Please enter rental week: '))


car = ('Luxury', 'luxury', 'Midsize', 'midsize', 'Compact', 'compact')

if (carType in car) and (rentalDay <= 30) and rentalWeek >= 0:
    if carType == 'Luxury' or carType == 'luxury':
        luxury_price_days = rentalDay * 75
        luxury_price_weeks = rentalWeek * 400
        total_luxury_price = luxury_price_days + luxury_price_weeks
        print(f'{carType} is your car type, renting {rentalWeek} weeks and {rentalDay} days,', end=' ')
        print(f'for a price of ${total_luxury_price} dollars.')
    

    if carType == 'Midsize' or carType == 'midsize':
        midsize_price_days = rentalDay * 50
        midsize_price_weeks = rentalWeek * 300
        total_midsize_price = midsize_price_days + midsize_price_weeks
        print(f'{carType} is your car type, renting {rentalWeek} weeks and {rentalDay} days,', end=' ')
        print(f'for a price of ${total_midsize_price} dollars.')
        
        
    if carType == 'Compact' or carType == 'compact':
        compact_price_days = rentalDay * 30
        compact_price_weeks = rentalWeek * 150
        total_compact_price = compact_price_days + compact_price_weeks
        print(f'{carType} is your car type, renting {rentalWeek} weeks and {rentalDay} days,', end=' ')
        print(f'for a price of ${total_compact_price} dollars.')
    
 
elif (carType != car) or rentalDay > 30 or rentalWeek < 0:
        print('invalid input, please check input again')
  
        

        
        
       
        
        
        
    
