def factorials(n):

    dict1 = {}
    fact = 1
    for i in range(1, n+1):
        fact *= i 
        dict1[i] = fact 
    
    return dict1 


if __name__ == "__main__":
    
    print(factorials(5))