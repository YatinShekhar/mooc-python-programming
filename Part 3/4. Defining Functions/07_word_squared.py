def squared(word, square):
    length = (square**2)//len(word) + 1
    word = word * length

    count = 0
    for i in range(square):
        new_word = []
        for j in range(count, count+square):
            new_word.append(word[j])
        print("".join(new_word))
        count += square

if __name__ == "__main__":
    squared("aybabtu", 5)