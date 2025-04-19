def line(integer, string):
    if string == "":
        print("*"*integer)
    else:
        print(string[0]*integer)

if __name__ == "__main__":
    
    line(5, "x")