def no_shouting(items):

    new_items = []
    for i in items:
        if i.isupper():
            continue 
        else:
            new_items.append(i)
    
    return new_items 


if __name__ == "__main__":
    
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    print(no_shouting(my_list))