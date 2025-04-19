word = input("Please type in a word: ")
character = input("Please type in a character: ")

position = word.find(character)

result = word[position: position+3]

if len(result) == 3:
    print(result)