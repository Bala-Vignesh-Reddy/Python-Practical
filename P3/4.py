# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

sal = int(input("Enter the salary:"))
yos = int(input("Enter the year of service:"))
bonus = 0
if yos > 5:
    bonus = sal * 0.05 
else:
    print("Bonus is only applicable for above 5 years")

print("Net Bonus\n",bonus)
