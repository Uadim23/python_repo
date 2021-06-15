#  Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
#  принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.matrix]))

    def __add__(self, other):
        for a in range(len(self.matrix)):
            for b in range(len(other.matrix[a])):
                self.matrix[a][b] = self.matrix[a][b] + other.matrix[a][b]
        return Matrix(self.matrix)


m_1 = Matrix([[31, 22], [37, 43], [51, 86]])
m_2 = Matrix([[31, 22], [37, 43], [51, 86]])
m_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
#print(m)
#print(m_2)
#print(m_3)
print(m_1 + m_2)