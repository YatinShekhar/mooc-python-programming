def sum_of_positives(items):

    sum = 0
    for i in items:
        if i > 0:
            sum += i 
    
    return sum 


if __name__ == "__main__":
    
    items = [1, -2, 3, -4, 5]
    a = sum_of_positives(items)
    print(f"The result is {a}")