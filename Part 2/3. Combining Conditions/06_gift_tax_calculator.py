value = int(input("Value of gift: "))

if value < 5000:
    lower_limit_tax = 0
    exceding_part_tax = 0
elif value >= 5000 and value < 25000:
    lower_limit_tax = 100
    exceding_part_tax = (value - 5000) * 0.08
elif value >= 25000 and value < 55000:
    lower_limit_tax = 1700
    exceding_part_tax = (value - 25000) * 0.10
elif value >= 55000 and value < 200000:
    lower_limit_tax = 4700
    exceding_part_tax = (value - 55000) * 0.12
elif value >= 200000 and value < 1000000:
    lower_limit_tax = 22100
    exceding_part_tax = (value - 200000) * 0.15
elif value >= 1000000:
    lower_limit_tax = 142100
    exceding_part_tax = (value - 1000000) * 0.17

tax = lower_limit_tax + exceding_part_tax

if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")