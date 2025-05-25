import math

def hypotenuse(leg1, leg2):
    h = math.sqrt(leg1**2 + leg2**2)
    return h 

if __name__ == "__main__":
    print(hypotenuse(3,4))