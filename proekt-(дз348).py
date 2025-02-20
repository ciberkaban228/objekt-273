# Функція для відображення поля
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Функція для перевірки на перемогу
def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтальні
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикальні
        [0, 4, 8], [2, 4, 6]              # діагоналі
    ]
    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

# Функція для перевірки на нічию
def check_draw(board):
    return "-" not in board

# Функція для ходу комп'ютера
def computer_move(board):
    empty_spaces = [i for i in range(9) if board[i] == "-"]
    return random.choice(empty_spaces)

# Основна функція гри
def play_game():
    board = ["-"] * 9  # Створення порожнього поля
    current_player = "X"  # Гравець починає першим

    while True:
        print_board(board)

        if current_player == "X":  # Хід гравця
            move = int(input("Виберіть клітинку (1-9): ")) - 1
            if board[move] != "-":
                print("Ця клітинка вже зайнята, виберіть іншу.")
                continue
            board[move] = "X"
        else:  # Хід комп'ютера
            print("Хід комп'ютера...")
            move = computer_move(board)
            board[move] = "O"

        # Перевірка на перемогу
        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} виграв!")
            break

        # Перевірка на нічию
        if check_draw(board):
            print_board(board)
            print("Нічия!")
            break

        # Зміна гравця
        current_player = "O" if current_player == "X" else "X"

# Запуск гри
if __name__ == "__main__":
    play_game()
