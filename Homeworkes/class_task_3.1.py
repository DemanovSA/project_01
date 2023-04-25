# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступны следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)


class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[1 for j in range(self.rows)] for _ in range(self.columns)]

    def set_value(self, row, column, value):
        if row < 1 or row > self.rows or column < 1 or column > self.columns:
            while row >= self.rows:
                self.matrix.append([1 for j in range(self.columns)])
                self.rows += 1
            while column >= self.columns:
                for i in range(self.rows):
                    self.matrix[i].append(None)
                    self.columns += 1

        self.matrix[row-1][column-1] = value

    def get_value(self, row, column):
        if row < 1 or row > self.rows or column < 1 or column > self.columns:
            raise IndexError("Invalid row or column")
        return self.matrix[row-1][column-1]
    def get_matrix(self):
        return self.matrix
    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns
n=int(input("Введите количество строк: "))
m=int(input("Введите количество столбцов: "))    
matrix = Matrix(n, m)
print(matrix.get_rows())     
print(matrix.get_columns())
ans = matrix.get_matrix()
print(f'Матрица из {ans[0][0]}:\n - количество строк {matrix.get_rows()};\n - количество столбцов {matrix.get_columns()}.')  

# matrix.set_value(1, 1, 10)
# matrix.set_value(2, 3, 20)
# matrix.set_value(3, 2, 30)
for i in range(matrix.get_rows()):
    print(ans[i])  
print(matrix.get_matrix())

# Отличное решение
# Этого я и ожидал)
# У меня есть еще вариант через словари

class Table:
    def __init__(self, colnames: list):
        self.colnames = colnames
        self.rows = []

    def add_row(self, row: dict):
        if any(colname not in tuple(row) for colname in self.colnames):  # хотя бы один элемент не соответствует
            print('Такой колонки нет')
        else:
            self.rows.append(row)

    def get_column(self, colname):
        if (colname not in self.colnames):
            print('Такой колонки нет')
        return [r[colname] for r in self.rows]


    def sum(self, colname: str):
        if colname not in self.colnames:
          print('Неправильный формат')
        return sum([r[colname] for r in self.rows])



table1 = Table([1, 2])
table1.add_row({1: 10, 2: 20})
table1.add_row({1: 20, 2: 400})
table1.add_row({1: 30, 2: 600})
table1.add_row({1: 40, 2: 800})
print(table1.get_column(1))
print(table1.get_column(2))
print(table1.rows)


