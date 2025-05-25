import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birth_date = datetime.datetime(year, month, day)
new_millenium = datetime.datetime(1999, 12, 31)

difference = new_millenium - birth_date 

if difference.days < 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {difference.days} days old on the eve of the new millennium.")