word = input("Please type in a word: ")
character = input("Please type in a character: ")

while True:
    if len(word) == 0:
        break

    if character == word[0]:
        result = word[0:3]

        if len(result) == 3:
            print(result)

    word = word[1:]