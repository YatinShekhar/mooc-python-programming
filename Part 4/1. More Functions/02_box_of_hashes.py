def line(integer, string):

    if string == "":
        print("*"*integer)
    else:
        print(string[0]*integer)


def box_of_hashes(height):

    num = 1
    while num <= height:
        line(10, "#")
        num += 1


if __name__ == "__main__":
    
    box_of_hashes(5)
