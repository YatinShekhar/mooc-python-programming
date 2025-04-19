num = 0
while True:
    pin = int(input("PIN: "))
    num += 1
    if pin == 4321:
        break
    else:
        print("Wrong")

if num == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {num} attempts")