word = input("Word: ")

empty_spaces = (28 - len(word))//2

string1 = "*"*30

if len(word)%2 == 0:
    string2 = "*" + " "*empty_spaces + word + " "*empty_spaces + "*"
else:
    string2 = "*" + " "*empty_spaces + word + " "*(empty_spaces+1) + "*"

print(string1)
print(string2)
print(string1)