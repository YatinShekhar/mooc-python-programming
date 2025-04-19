def length_of_longest(items):

    longest = ""
    for i in items:
        if len(i) > len(longest):
            longest = i 
    
    return len(longest)


if __name__ == "__main__":
    
    my_list = ["first", "second", "fourth", "eleventh"]
    print(length_of_longest(my_list))