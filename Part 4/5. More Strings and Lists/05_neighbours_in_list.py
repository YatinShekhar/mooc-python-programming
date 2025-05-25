def longest_series_of_neighbours(ls):

    max_len = 1
    current_len = 1

    for i in range(1, len(ls)):
        if abs(ls[i] - ls[i - 1]) == 1:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1

    return max_len


if __name__ == "__main__":
    my_list = [5, 3, 4, 2, 3, 1, 2, 3, 9, 8, 7, 8, 7, 6, 7, 6]
    print(longest_series_of_neighbours(my_list))