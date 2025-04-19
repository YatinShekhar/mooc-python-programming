def no_vowels(word):

    new_word = ""
    for i in word:
        if i not in ["a", "e", "i", "o", "u"]:
            new_word += i 
    
    return new_word


if __name__ == "__main__":
    
    word = "this is an example"
    print(no_vowels(word))