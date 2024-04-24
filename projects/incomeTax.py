# Step 1 Input wages, taxable interest, unemployment compensation, status and taxes in integers.
wages, taxable_interest, unemployment_compensation, status, taxes_withheld = [int(user_input) for user_input in
                                                                              input().split()]
# calculates AGI
AGI = (wages + taxable_interest + unemployment_compensation)
# prints AGI
print("AGI: ${:,}".format(AGI))

# check if AGI greater than 120000
if AGI > 120000:
    print("Error: Income too high to use this form")

# Step 2 identify deduction amount based on status
deduction_amount = 0

# check if status is 1 or 2, if not set to status 1
if not status == 1 and not status == 2:
    status = 1

# sets the deduction amount
if status == 1:
    deduction_amount = 12000
elif status == 2:
    deduction_amount = 24000

# Calculates taxable income (AGI - deduction).
taxable_income = AGI - deduction_amount

# Set taxable income to zero if negative.
if taxable_income < 0:
    taxable_income = 0

# Outputs deduction and taxable income.
print("Deduction: ${:,}".format(deduction_amount))
print("Taxable income: ${:,}".format(taxable_income))
# Step 3 Calculates tax amount based on exemption and taxable income
tax_amount = 0
# tax for single
if status == 1:
    if taxable_income > 0 and taxable_income <= 10000:
        tax_amount = taxable_income * 0.10
    elif taxable_income >= 10001 and taxable_income <= 40000:
        tax_amount = 1000 + (taxable_income - 10000) * 0.12
    elif taxable_income >= 40001 and taxable_income <= 85000:
        tax_amount = 4600 + (taxable_income - 40000) * 0.22
    elif taxable_income > 85000:
        tax_amount = 14500 + (taxable_income - 85000) * 0.24
# tax for married
elif status == 2:
    if taxable_income > 0 and taxable_income <= 20000:
        tax_amount = taxable_income * 0.10
    elif taxable_income >= 20001 and taxable_income <= 80000:
        tax_amount = 2000 + (taxable_income - 20000) * 0.12
    elif taxable_income > 80000:
        tax_amount = 9200 + (taxable_income - 80000) * 0.22

# prints federal tax
tax_amount = round(tax_amount)
print("Federal Tax: ${:,}".format(tax_amount))

# Step 4 Calculates amount of tax due (tax - withheld).
tax_due = tax_amount - taxes_withheld

# taxpayer receives a refund if tax due is negative. Outputs tax due or tax refund as positive values.
if tax_due < 0:
    print("Tax refund: ${:,}".format(abs(tax_due)))
