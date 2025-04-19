def histogram(a):

    list1 = list(a)
    dict1 = {}

    for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
        
    for i in dict1:
        dict1[i] = dict1[i]*"*"
        print(f"{i} {dict1[i]}")


if __name__ == "__main__":
    
    histogram("abba")