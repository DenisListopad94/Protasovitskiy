# 1. Определить класс «Шахматная фигура» с ее координатами на шахматной доске,
# ее цветом (черный или белый), виртуальным методом «битья» другой фигуры,
# и унаследовать от него классы, соответствующие шахматным фигурам «Ферзь», «Пешка», «Конь».
# Написать виртуальные методы «битья» другой фигуры,
# которые принимают координаты другой фигуры и определяют,
# может ли данная фигура «бить» фигуру с теми (принятыми) координатами.
class ChessPiece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y


class Queen(ChessPiece):
    def can_attack(self, other_x, other_y):
        return self.x == other_x or self.y == other_y or (self.x - other_x) == (self.y - other_y)


class Pawn(ChessPiece):
    def can_attack(self, other_x, other_y):
        return (self.x - other_x) == 1 and (self.y - other_y) == 1 and self.color == 'white'


class Horse(ChessPiece):
    def can_attack(self, other_x, other_y):
        return (self.x - other_x) == 2 and (self.y - other_y) == 1 or \
            (self.x - other_x) == 1 and (self.y - other_y) == 2


# Пример использования
queen_figure = Queen('white', 1, 1)
pawn_figure = Pawn('black', 2, 2)
horse_figure = Horse('white', 3, 3)

print('Queen moves:')
print('Can Queen attack Pawn?', queen_figure.can_attack(pawn_figure.x, pawn_figure.y))
print('Can Queen attack Horse?', queen_figure.can_attack(horse_figure.x, horse_figure.y))

print('\nPawn moves:')
print('Can Pawn attack Queen?', pawn_figure.can_attack(queen_figure.x, queen_figure.y))
print('Can Pawn attack Horse?', pawn_figure.can_attack(horse_figure.x, horse_figure.y))

print('\nHorse moves:')
print('Can Horse attack Queen?', horse_figure.can_attack(queen_figure.x, queen_figure.y))
print('Can Horse attack Pawn?', horse_figure.can_attack(pawn_figure.x, pawn_figure.y))