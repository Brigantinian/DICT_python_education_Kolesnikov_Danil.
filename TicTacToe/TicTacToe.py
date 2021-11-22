import random



class TicTacToe:


    def __init__(self):
        self.pole = []

    def create_pole(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.pole.append(row)

    def get_random_first_igrok(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, igrok):
        self.pole[row][col] = igrok

    def is_igrok_win(self, igrok):
        win = None
        n = len(self.pole)
        for y in range(n):
            win = True
            for x in range(n):
                if self.pole[y][x] != igrok:
                    win = False
                    break
            if win:
                return win


        for y in range(n):
            win = True
            for x in range(n):
                if self.pole[x][y] != igrok:
                    win = False
                    break
            if win:
                return win
            if len(self.pole) == 2:
                break


        win = True
        for y in range(n):
            if self.pole[y][y] != igrok:
                win = False
                break
        if win:
            return win

        win = True
        for y in range(n):
            if self.pole[y][n - 1 - y] != igrok:
                win = False
                break
        if win:
            return win
        return False

    def is_pole_filled(self):
     for row in self.pole:
        for item in row:
          if item == '-':
            return False
        return True



    def swap_igrok_turn(self, igrok):
        return 'X' if igrok == 'O' else 'O'

    def show_pole(self):
        for row in self.pole:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_pole()

        igrok = 'X' if self.get_random_first_igrok() == 1 else 'O'
        self.show_pole()
        while True:
            print(f"igrok {igrok} turn")

            row, col = list(
                map(int, input("Enter cells: ").split()))
            print()
            self.fix_spot(row - 1, col - 1, igrok)
            self.show_pole()
            if self.is_igrok_win(igrok):
                print(f"Player { igrok } wins the game!")
                break

            if self.is_pole_filled():
                print("Match Draw!")
                break
            igrok = self.swap_igrok_turn(igrok)


        print()
        # self.show_pole()


tic_tac_toe = TicTacToe()
tic_tac_toe.start()