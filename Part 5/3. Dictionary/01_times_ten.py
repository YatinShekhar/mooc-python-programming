def times_ten(start_index, end_index):

    dict1 = {}
    for i in range(start_index, end_index+1):
        dict1[i] = i * 10

    return dict1 


if __name__ == "__main__":
    
    print(times_ten(3,6))