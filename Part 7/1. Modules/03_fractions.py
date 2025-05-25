import fractions

def fractionate(amount):
    list1 = []
    for i in range(amount):
        value = fractions.Fraction(1,amount)
        list1.append(value)

    return list1 

if __name__ == "__main__":
    print(fractionate(5))