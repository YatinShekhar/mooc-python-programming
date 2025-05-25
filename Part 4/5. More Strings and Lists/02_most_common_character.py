def most_common_character(word):
    new_dict = {}
    for i in word:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
        
    for key, value in new_dict.items():
        if value == max(new_dict.values()):
            return key

if __name__ == "__main__":
    print(most_common_character('first_string'))