def list_sum(items1, items2):

    items3 = []
    for i in range(0, len(items1)):
        item1 = items1[i]
        item2 = items2[i]
        items3.append(item1+item2)

    return items3 


if __name__ == "__main__":
    
    a = [1,2,3,4]
    b = [5,6,7,8]

    print(list_sum(a,b))