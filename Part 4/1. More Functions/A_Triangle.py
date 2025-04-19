def line(integer, string):

    if string == "":
        print("*"*integer)
    else:
        print(string[0]*integer)

def triangle(size):

    num = 1
    while num <= size:
        line(num, "#")
        num += 1


if __name__ == "__main__":
    
    triangle(5)