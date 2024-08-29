import random


class TicTacToe:
    def __init__(self):
        self.board = ["-"] * 9
        self.player = "X"
        self.winner = None
        self.game_running = True

    def print_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))
            if i < 6:
                print("_________")



    def player_input(self):
        while True:
            try:
                inp = int(input(f"Player {self.player}, select a spot between 1-9: "))-1
                if 0 <= inp <= 9 and self.board[inp] == "-":
                    self.board[inp] = self.player
                    break
                else:
                    print("Invalid spot!")
            except ValueError:
                print("Invalid spot!, Enter a number between 1-9")



    def check_winner(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  #rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  #columns
            [0, 4, 8], [2, 4, 6]  #diagonals
        ]

        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "-":
                self.winner = combo[0]
                return True
        return False


    def check_tie(self):
        return "-" not in self.board

    def switch_player(self):
        self.player = "O" if self.player == "X" else "X"

    def computer_turn(self):
        empty_spots = [i for i, spot in enumerate(self.board) if spot == "-"]
        if empty_spots:
            self.board[random.choice(empty_spots)] = "O"

    def play(self):
        while self.game_running:
            self.print_board()

            if self.player == "X":
                self.player_input()
            else:
                self.computer_turn()

            if self.check_winner():
                self.print_board()
                print(f"Player {self.player} wins!")
                self.game_running = False

            elif self.check_tie():
                self.print_board()
                print(f"Tie!")
                self.game_running = False
            else:
                self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
