def all_the_longest(items):

    new_items = []
    item = ""
    for i in items:
        if len(i) > len(item):
            new_items.clear()
            new_items.append(i)
            item = i
        elif len(i) == len(item):
            new_items.append(i)
            item = i
    
    return new_items 


if __name__ == "__main__":
    
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print(all_the_longest(my_list))