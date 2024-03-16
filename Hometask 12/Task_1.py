# 1. Определить класс «Шахматная фигура» с ее координатами на шахматной доске,
# ее цветом (черный или белый), виртуальным методом «битья» другой фигуры,
# и унаследовать от него классы, соответствующие шахматным фигурам «Ферзь», «Пешка», «Конь».
# Написать виртуальные методы «битья» другой фигуры,
# которые принимают координаты другой фигуры и определяют,
# может ли данная фигура «бить» фигуру с теми (принятыми) координатами.
class ChessPiece:
    def __init__(self,
                 color: str,
                 x: int,
                 y: int) -> None:
        self.color = color
        self.x = x
        self.y = y

    def move(self,
             x: int,
             y: int) -> None:
        """
        Get boardwalk of some figure
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y


class Queen(ChessPiece):
    def can_attack(self, figure: ChessPiece) -> bool:
        """
        get Queen can attack some figure
        :param figure: cls
        :return: bool
        """
        return self.x == figure.x or self.y == figure.y or (self.x - figure.x) == (self.y - figure.y)


class Pawn(ChessPiece):
    def can_attack(self, figure: ChessPiece) -> bool:
        """
        get Pawn can attack some figure
        :param figure: cls
        :return: bool
        """
        return (self.x - figure.x) == 1 and (self.y - figure.y) == 1 and self.color == 'white'


class Horse(ChessPiece):
    def can_attack(self, figure: ChessPiece) -> bool:
        """
        get Horse can attack some figure
        :param figure: cls
        :return: bool
        """
        return (self.x - figure.x) == 2 and (self.y - figure.y) == 1 or \
            (self.x - figure.x) == 1 and (self.y - figure.y) == 2


# Пример использования
queen_figure = Queen('white', 1, 1)
pawn_figure = Pawn('black', 2, 2)
horse_figure = Horse('white', 3, 3)

print('Queen moves:')
print('Can Queen attack Pawn?', queen_figure.can_attack(figure=pawn_figure))
print('Can Queen attack Horse?', queen_figure.can_attack(figure=horse_figure))

print('\nPawn moves:')
print('Can Pawn attack Queen?', pawn_figure.can_attack(figure=queen_figure))
print('Can Pawn attack Horse?', pawn_figure.can_attack(figure=horse_figure))

print('\nHorse moves:')
print('Can Horse attack Queen?', horse_figure.can_attack(figure=queen_figure))
print('Can Horse attack Pawn?', horse_figure.can_attack(figure=pawn_figure))
