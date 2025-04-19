def range_of_list(my_list):

    diff = max(my_list) - min(my_list)
    return diff


if __name__ == "__main__":
    
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)