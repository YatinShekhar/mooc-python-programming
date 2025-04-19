def greatest_number(x,y,z):

    if x > y: 
        if y > z:
            return x
        else:
            if x > z:
                return x
            else:
                return z 
    else:
        if y > z:
            return y 
        else:
            return z


if __name__ == "__main__":

    greatest = greatest_number(5, 4, 8)
    print(greatest)