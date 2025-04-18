num = int(input("Please type in a number: "))

list1 = [i for i in range(1, num+1)]

for i in list1[1::2]:
        print(i)
        print(list1.index(i))

if num%2 != 0:
    print(list1[-1])