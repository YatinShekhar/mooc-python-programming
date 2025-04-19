num = int(input("Please type in a number: "))

while num > 0:

    n = 1
    factorial = 1

    while n <= num:
        factorial *= n
        n += 1
    
    print(f"The factorial of the number {num} is {factorial}")

    num = int(input("Please type in a number: "))

else:
    print("Thanks and bye!")