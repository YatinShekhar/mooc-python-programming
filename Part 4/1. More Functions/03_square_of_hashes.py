def line(integer, string):

    if string == "":
        print("*"*integer)
    else:
        print(string[0]*integer)


def square_of_hashes(size):

    num = 1
    while num <= size:
        line(size, "#")
        num += 1


if __name__ == "__main__":
    
    square_of_hashes(5)