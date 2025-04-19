def palindromes(word):

    if word == word[::-1]:
        return True
    else:
        return False


while True:
    word = input("Please type in a palindrome: ")
    
    if palindromes(word) == True:
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")