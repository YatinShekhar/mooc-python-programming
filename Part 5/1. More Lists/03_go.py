def who_won(game_board):

    count_player_1 = 0
    count_player_2 = 0
    for i in game_board:
        count_player_1 += i.count(1)
        count_player_2 += i.count(2)

    if count_player_1 > count_player_2:
        return 1
    elif count_player_2 > count_player_1:
        return 2
    else:
        return 0
    

if __name__ == "__main__":
    
    go_board =[
    [0, 1, 0, 2, 0, 0, 1, 2, 0],
    [2, 0, 1, 0, 2, 1, 0, 0, 1],
    [0, 2, 0, 1, 0, 0, 2, 1, 0],
    [1, 0, 2, 0, 1, 2, 0, 0, 0],
    [0, 1, 0, 0, 2, 0, 1, 2, 0],
    [0, 0, 2, 1, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 1, 2, 0, 0],
    [0, 1, 2, 0, 1, 0, 0, 2, 1],
    [2, 0, 0, 1, 0, 2, 1, 0, 0]
    ]
    print(who_won(go_board))