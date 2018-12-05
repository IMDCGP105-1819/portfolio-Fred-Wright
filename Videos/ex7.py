print("Enter your annual salary:")
salary = int(input())

monthly_salary = salary / 12

r = 0.04

print("Enter the percent of your salary to save, as a decimal")
decimal_savings = float(input())

print ("Enter the cost of your dream home:")
total_cost = int(input())

total_deposit = total_cost / 5
#maths#

portion_saved = decimal_savings * salary / 12 #=1000
current_savings = 0
months = 0
while current_savings <= total_deposit:


    savingsIntrest = (current_savings * r) / 12
    monthly_savings = (monthly_salary * decimal_savings) + savingsIntrest
    current_savings = monthly_savings + current_savings
    months = months + 1

    print("monthlySavings     ", monthly_savings)
    print (months)
