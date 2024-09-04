# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

sal = int(input("Enter the salary:"))
yos = int(input("Enter the year of service:"))
bonus = 1
if yos > 5:
    bonus = sal * 0.05 

print("Net Bonus\n", bonus)
