def chessboard(length):

    x = 1

    while x <= length:

        if x%2 != 0:
            square = 1
        else:
            square = 0

        y = 1

        while y <= length:

            print(square, end= "")

            if square == 0:
                square = 1
            else:
                square = 0

            y += 1

        print()
        x += 1


if __name__ == "__main__":
    chessboard(6)