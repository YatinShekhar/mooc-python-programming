days = int(input("How many times a week do you eat at the student cafeteria? "))
lunch = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))
print()
daily = (days * lunch + groceries)/7
weekly = days * lunch + groceries
print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")