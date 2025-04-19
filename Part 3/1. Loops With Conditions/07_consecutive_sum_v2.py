limit = int(input("Limit: "))
n = 1
sum = 0
addition = ""
while sum < limit:
    addition += str(n)
    sum += n
    
    if sum < limit:
        addition += " + "
        
    n += 1

print(f"The consecutive sum: {addition} = {sum}")