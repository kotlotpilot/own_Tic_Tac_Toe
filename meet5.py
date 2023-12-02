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

    def __init__(self):
        self.field = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.step_number = 0
        self.score = {'X': 0, 'O': 0}

    def has_steps(self) -> bool:
        return any(cell not in [X_CELL, O_CELL] for row in self.field for cell in row)

    def get_step(self) -> int:
        while True:
            try:
                print(f"Хід {X_CELL if self.step_number % 2 == 0 else O_CELL}:")
                choice = int(input())
                if 1 <= choice <= 9 and self.field[(choice - 1) // 3][(choice - 1) % 3] not in [X_CELL, O_CELL]:
                    return choice
                else:
                    print("Номер клітинки має бути від 1 до 9 і не повинен бути зайнятий")
            except ValueError:
                print("Помилка")

    def set_step(self, choice: int):
        symbol = X_CELL if self.step_number % 2 == 0 else O_CELL
        row, col = (choice - 1) // 3, (choice - 1) % 3

        self.field[row][col] = symbol
        self.step_number += 1

    def check_winning_conditions(self) -> str:
        for combination in self.WINNING_COMBINATIONS:
            cells = [self.field[row][col] for row, col in combination]
            if all(cell == X_CELL for cell in cells):
                self.score['X'] += 1
                return 'Переможець X'
            elif all(cell == O_CELL for cell in cells):
                self.score['O'] += 1
                return 'Переможець O'
        return None


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


if __name__ == '__main__':
    while True:
        game = Game()
        while game.has_steps():
            print_board(game.field)
            game.set_step(game.get_step())
            result = game.check_winning_conditions()

            if result:
                game.winner = result
                break
        print_board(game.field)
        print(game.winner or 'Нічия')
        print(f"Рахунок: X - {game.score['X']}, O - {game.score['O']}")

        play_again_ = input("Грати ще раз (так/ні)? ").lower()
        if play_again_ != 'так':
            print("Дякую за гру!")
            break
