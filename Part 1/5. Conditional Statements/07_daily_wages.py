hourly_wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")

if day == "Sunday":
    hourly_wage = hourly_wage * 2


daily_wages = hourly_wage * hours 

print(f"Daily wages: {daily_wages} euros")