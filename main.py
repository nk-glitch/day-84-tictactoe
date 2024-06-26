grid_dict = {
    "top left": "",
    "top middle": "",
    "top right": "",
    "middle left": "",
    "middle middle": "",
    "middle right": "",
    "bottom left": "",
    "bottom middle": "",
    "bottom right": ""
}

#gameloop

game_continues = True
while game_continues:

    row1 = [grid_dict["top left"], grid_dict["top middle"], grid_dict["top right"]]
    row2 = [grid_dict["middle left"], grid_dict["middle middle"], grid_dict["middle right"]]
    row3 = [grid_dict["bottom left"], grid_dict["bottom middle"], grid_dict["bottom right"]]


    def print_rows():
        print(row1)
        print(row2)
        print(row3)


    def check_for_win():
        global game_continues
        if row1[0] == row1[1] == row1[2] == "X" or row1[0] == row1[1] == row1[2] == "Y":
            print(f"{row1[0]} has won the game")
            game_continues = False
        if row2[0] == row2[1] == row2[2] == "X" or row2[0] == row2[1] == row2[2] == "Y":
            print(f"{row1[0]} has won the game")
            game_continues = False
        if row3[0] == row3[1] == row3[2] == "X" or row3[0] == row3[1] == row3[2] == "Y":
            print(f"{row1[0]} has won the game")
            game_continues = False
        if row3[0] == row2[0] == row1[0] == "X" or row3[0] == row2[0] == row1[0] == "Y":
            print(f"{row1[0]} has won the game")
            game_continues = False
        if row3[1] == row2[1] == row1[1] == "X" or row3[1] == row2[1] == row1[1] == "Y":
            print(f"{row1[1]} has won the game")
            game_continues = False
        if row3[2] == row2[2] == row1[2] == "X" or row3[2] == row2[2] == row1[2] == "Y":
            print(f"{row1[2]} has won the game")
            game_continues = False
        if row1[0] == row2[1] == row3[2] == "X" or row1[0] == row2[1] == row3[2] == "Y":
            print(f"{row1[0]} has won the game")
            game_continues = False
        if row3[0] == row2[1] == row1[2] == "X" or row3[0] == row2[1] == row1[2] == "Y":
            print(f"{row3[0]} has won the game")
            game_continues = False


    print_rows()

    check_for_win()

    if game_continues:
        user_input = input("Player1, Choose a square: ")
        grid_dict[user_input] = "X"

        row1 = [grid_dict["top left"], grid_dict["top middle"], grid_dict["top right"]]
        row2 = [grid_dict["middle left"], grid_dict["middle middle"], grid_dict["middle right"]]
        row3 = [grid_dict["bottom left"], grid_dict["bottom middle"], grid_dict["bottom right"]]

        print_rows()

        check_for_win()

        user_input = input("Player2, Choose a square: ")
        grid_dict[user_input] = "O"
