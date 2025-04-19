def even_numbers(items):

    even_items = []
    for i in items:
        if i%2 == 0:
            even_items.append(i)
        
    return even_items
    

if __name__ == "__main__":
    
    my_list = [1, 2, 3, 4, 5]
    print(even_numbers(my_list))