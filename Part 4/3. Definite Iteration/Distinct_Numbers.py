def distinct_numbers(items):

    new_items = []
    for i in items:
        if i not in new_items:
            new_items.append(i)
    
    new_items = sorted(new_items)

    return new_items


if __name__ == "__main__":
    
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))