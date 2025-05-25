def matrix_sum():
    with open("matrix.txt") as new_file:
        sum = 0
        for i in new_file:
            i = i.replace("\n", "")
            list1 = i.split(",")
            for j in list1:
                sum += int(j)

    return sum 

def matrix_max():
    with open("matrix.txt") as new_file:
        max = float("-inf")
        for i in new_file:
            i = i.replace("\n", "")
            list1 = i.split(",")
            for j in list1:
                if int(j) > max:
                    max = int(j)

    return max 

def row_sums():
    with open("matrix.txt") as new_file:
        list1 = []
        for i in new_file:
            sum = 0
            i = i.replace("\n", "")
            list2 = i.split(",")
            for j in list2:
                sum += int(j)
                
            list1.append(sum)

    return list1

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())