def double_items(items):

    doubled_items = []
    for i in items:
        doubled_items.append(i*2)
    
    return doubled_items


if __name__ == "__main__":
    
    my_list = [2, 3, 4, 5, 11, -4]
    print(double_items(my_list))