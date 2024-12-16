#Personal fincance calculator
#defining all the prompts

monthly_income = float(input("Enter your monthly income"))
monthly_expenses = float(input("Enter your monthly expense"))

#Monthly savings 
monthly_saving = monthly_income - monthly_expenses

#Projected savings

projected_savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

#printing the output

print(f"Your monthly saving are ${monthly_saving)")
print(f"Your projected savings after one year, with interest, is: ${projected_savings}")

