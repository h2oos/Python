def futureInvestmentValue(investmentAmount, monthlyInterest, years):
    print('Year''\t' "Future Value")

    for i in range(20):
        rate = monthlyInterest/1200
        percent = ((investmentAmount*((1+rate))**(12*(i+1))))
        print(i+1, '\t'"%.2f"%percent)

investmentAmount = int(input('Enter the investment amount: '))
monthlyInterest = int(input('Enter annual interest in percent: '))

futureInvestmentValue(investmentAmount, monthlyInterest, 5 )

