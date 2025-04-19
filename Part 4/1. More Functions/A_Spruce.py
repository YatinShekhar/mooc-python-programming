def spruce(size):

    print("a spruce!")
    n = 1
    m = 1
    while n <= size:
        print(" "*(size-n), end="")
        print("*"*m)
        n += 1
        m += 2
    print(" "*(size-1), end= "")
    print("*")


if __name__ == "__main__":
    
    spruce(5)