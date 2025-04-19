def everything_reversed(items):

    reversed_items = []
    for i in items[::-1]:
        reversed_items.append(i[::-1])

    return reversed_items 


if __name__ == "__main__":
    
    my_list = ["Hi", "there", "example", "one more"]
    print(everything_reversed(my_list))