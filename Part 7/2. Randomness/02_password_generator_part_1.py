import random 

def generate_password(length):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    password = random.sample(alphabets, length)
    password = "".join(password)

    return password 

if __name__ == "__main__":
    print(generate_password(10))