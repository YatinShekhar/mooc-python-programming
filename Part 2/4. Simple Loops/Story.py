sentence = ""
previous_word = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or previous_word == word:
        break 
    else:
        previous_word = word
        sentence += word + " "

print(sentence)