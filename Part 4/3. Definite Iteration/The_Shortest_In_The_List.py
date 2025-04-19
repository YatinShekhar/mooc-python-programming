def shortest(items):

    shortest_item = items[0]
    for i in items:
        if len(i) < len(shortest_item):
            shortest_item = i 
    
    return shortest_item


if __name__ == "__main__":

    my_list = ["first", "second", "fourth", "eleventh"]
    print(shortest(my_list))