from typing import List, Tuple

X_CELL = "X"
O_CELL = "O"

class Game:
    WINNING_COMBINATIONS = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    def __init__(self, field=None, size=None):
        if field is None:
            self.field = self.create_field(size)
        else:
            self.field = field

        self.step_number: int = self.calculate_step_number()
        self.who_win = None
        self.winner = None

    def create_field(self, size: int) -> List[List[str]]:
        field = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        return field

    def calculate_step_number(self) -> int:
        return 0

    def has_steps(self) -> bool:
        for row in self.field:
            for cell in row:
                if cell not in [X_CELL, O_CELL]:
                    return True
        return False

    def get_step(self) -> int:
        while True:
            try:
                print(f"Хід {X_CELL if self.step_number % 2 == 0 else O_CELL}:")
                a = int(input())
                if 1 <= a <= 9:
                    return a
                else:
                    print("Номер клітинки має бути від 1 до 9")
            except ValueError:
                print("Помилка")

    def set_step(self, choice: int, should_i_place_x: bool):
        symbol = X_CELL if should_i_place_x else O_CELL
        row, col = self.get_coordinates(choice)

        if self.is_valid_move(row, col):
            self.field[row][col] = symbol
            self.step_number += 1
        else:
            print("Ця клітинка вже зайнята")

    def get_coordinates(self, a: int) -> Tuple[int, int]:
        if 1 <= a <= 9:
            row = (a - 1) // 3
            col = (a - 1) % 3
            return row, col
        else:
            raise ValueError("Номер клітинки має бути від 1 до 9")

    def is_valid_move(self, row: int, col: int) -> bool:
        if self.field[row][col] not in [X_CELL, O_CELL]:
            return True
        else:
            return False


    score = {'X':0, 'O':0}
    def check_winning_conditions(self) -> str:
        for combination in self.WINNING_COMBINATIONS:
            cells = [self.field[row][col] for row, col in combination]
            if all(cell == X_CELL for cell in cells):
                self.score['X'] += 1
                return f'Переможець X'
            elif all(cell == O_CELL for cell in cells):
                self.score['O'] += 1
                return f'Переможець O'
        return None


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

if __name__ == '__main__':
    play_again = True
    while play_again:
        game = Game()
        while game.has_steps():
            print_board(game.field)
            game.set_step(game.get_step(), game.step_number % 2 == 0)
            result = game.check_winning_conditions()

            if result:
                game.winner = result
                break
        print_board(game.field)
        if game.winner is None:
            print('Нічия')
        else:
            print(game.winner)
        print(f"Рахунок: X - {game.score['X']}, O - {game.score['O']}")
        while True:
            try:
                play_again_ = input("Грати ще раз (так/ні)? ").lower()
                if play_again_ == 'так':
                    break
                elif play_again_ == 'ні':
                    print("Дякую за гру!")
                    exit()
                else:
                    print("Введіть 'так' або 'ні'.")
            except ValueError:
                print("Помилка")