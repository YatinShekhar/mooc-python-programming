def read_fruits():
    with open("fruits.csv") as new_file:
        dict1 = {}
        for i in new_file:
            i = i.replace("\n", "")
            list1 = i.split(";")
            dict1[list1[0]] = float(list1[1])
            

    return dict1 

if __name__ == "__main__":
    print(read_fruits())