def first_word(sentence):

    pos = sentence.find(" ")
    return sentence[0:pos]
    

def second_word(sentence):
    
    pos = sentence.find(" ")
    sentence = sentence[pos+1:]
    pos = sentence.find(" ")
    if pos == -1:
        return sentence[0:]
    else:
        return sentence[0:pos]


def last_word(sentence):

    sentence = sentence[::-1]
    pos = sentence.find(" ")
    return sentence[0:pos][::-1]


if __name__ == "__main__":
    
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))