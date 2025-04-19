def remove_smallest(items):

    items.remove(min(items))


if __name__ == "__main__":
    
    my_list = [2, 4, 6, 1, 3, 5]
    remove_smallest(my_list)
    print(my_list)