def formatted(items):

    new_items = []
    for i in items:
        j = f"{i:.2f}"
        new_items.append(j)
    
    return new_items 

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    print(formatted(my_list))