def anagrams(word1, word2):

    if sorted(word1) == sorted(word2):
        return True
    else:
        return False 


if __name__ == "__main__":
    
    word1 = "tomato"
    word2 = "potato"
    print(anagrams(word1, word2))