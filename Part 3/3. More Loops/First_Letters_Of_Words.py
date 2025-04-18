sentence = input("Please type in a sentence: ")

list1 = sentence.split(" ")

n = 0
while n < len(list1):
    print(list1[n][0])

    n += 1
