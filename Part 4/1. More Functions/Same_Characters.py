def same_chars(word, pos1, pos2):

    if pos1 >= len(word):
        return False 
    elif pos2 >= len(word):
        return False
    else:
        if word[pos1] == word[pos2]:
            return True 
        else:
            return False
        

if __name__ == "__main__":
    
    print(same_chars("coder", 1, 2))