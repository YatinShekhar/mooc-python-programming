import string 

def separate_characters(my_string):
    a1 = ""
    a2 = ""
    a3 = ""
    for i in my_string:
        if i in string.ascii_letters:
            a1 += i 
        elif i in string.punctuation:
            a2 += i
        else:
            a3 += i

    tuple1 = (a1, a2, a3)

    return tuple1 

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])