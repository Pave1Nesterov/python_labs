import random


def printMatrix(a):
    print()
    for row in a:
        for x in row:
            print('{:4d}'.format(x), end='')
        print()
    print()


def setMatrix(n):
    a = []
    while True:
        choice = int(
            input("1. Ввод значений с клавиатуры\n2. Заполнение матрицы рандомными значениями\nДействие: "))
        if choice == 1:
            for i in range(n):
                temp = []
                for j in range(n):
                    temp.append(int(input("a[{0}][{1}] = ".format(i, j))))
                a.append(temp)
            break
        elif choice == 2:
            x1 = int(input("Введите нижнюю границу: "))
            x2 = int(input("Введите верхнюю границу: "))
            a = [[random.randint(x1, x2) for i in range(n)] for j in range(n)]
            break
    return a


def shiftMatrix(matrix):
    length = n = len(matrix)
    x_start = y_start = d_x = d_y = 0
    x = 0
    y = -1
    temp_x = 1
    temp_y = 0
    for i in range(length // 2):
        j = 1
        d_row = 0
        d_column = 1
        temp0 = matrix[temp_x][temp_y]
        while j <= (2 * n + 2 * (n - 2)):
            if x_start <= x + d_row < n + d_x and y_start <= y + d_column < n + d_y:
                x += d_row
                y += d_column
                temp = matrix[x][y]
                matrix[x][y] = temp0
                temp0 = temp
                j += 1
            else:
                if d_column == 1:
                    d_column = 0
                    d_row = 1
                elif d_row == 1:
                    d_row = 0
                    d_column = -1
                elif d_column == -1:
                    d_column = 0
                    d_row = -1
                elif d_row == -1:
                    d_row = 0
                    d_column = 1
        n -= 2
        temp_x += 1
        temp_y += 1
        x_start += 1
        y_start += 1
        d_x += 1
        d_y += 1
    return matrix


def main():
    while True:
        n = int(input("Введите рязрядность матрицы: "))
        if n >= 2: break
    matrix = setMatrix(n)
    printMatrix(matrix)
    print("Осуществление кругового сдвига вправо на k элементов")
    while True:
        k = int(input("k = "))
        if k >= 0: break
    for i in range(k):
        matrix = shiftMatrix(matrix)
    printMatrix(matrix)


if __name__ == '__main__':
    main()
