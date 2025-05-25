def read_input(a, b, c):
    
    while True:
        try:
            a = int(a)
            if a > b and a < c:
                return a
            else:
                print(f"You must type in an integer between {b} and {c}")
                a = input("Please type in a number: ")
        
        except ValueError:
            print(f"You must type in an integer between {b} and {c}")
            a = input("Please type in a number: ")
        


if __name__ == "__main__":
    number = read_input(input("Please type in a number: "), 5, 10)
    print(f"You typed in: {number}")