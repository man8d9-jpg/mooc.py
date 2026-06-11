def play_turn(game_board: list, x: int, y: int, piece: str):
    if y not in range(3) or x not in range(3):
        return False
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True 
    
    return False

game_board = [["", "", "X"], ["", "", ""], ["", "", ""]]
print(play_turn(game_board, 2, 0, "X"))
print(game_board)
