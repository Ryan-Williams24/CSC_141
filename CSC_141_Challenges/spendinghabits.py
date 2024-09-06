# Ryan Williams
# Date: 9/4/24
# This is the starter file for CSC141 lab day 4

PA_TAX = 0.06
PRICE_OF_MEAL = 12.49

print("Lunch Spending Habits")
print("Amount spent on taxes per meal: " + str(PRICE_OF_MEAL*0.06))
print("Weekly spending before taxes: " + str(PRICE_OF_MEAL * 5) )
print("Weekly spending after taxes: " + str((PRICE_OF_MEAL*5)*(1+PA_TAX) ) )