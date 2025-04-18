string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

first_position = string.find(substring)

second_position = string.find(substring, first_position + len(substring))

if second_position == -1:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {second_position}.")