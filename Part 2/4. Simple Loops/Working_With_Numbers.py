print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum = 0
mean = 0
positive = 0
negative = 0
while True:
    num = int(input("Number: "))

    if num == 0:
        break
    
    count += 1
    sum += num
    mean = sum/count 
    
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")