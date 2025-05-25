def largest():
    with open("numbers.txt") as new_file:
        largest_number = float("-inf")
        for i in new_file:
            i = int(i.strip())
            if i > largest_number:
                largest_number = i
        
    return largest_number


if __name__ == "__main__":
    print(largest())