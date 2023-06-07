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
            while True:
                x1 = int(input("Введите нижнюю границу: "))
                x2 = int(input("Введите верхнюю границу: "))
                if x1 < x2:
                    break
                else:
                    print("Ошибка! Нижняя граница диапазона случайных значений должна быть меньше верхней")
            a = [[random.randint(x1, x2) for i in range(n)] for j in range(n)]
            break
    return a


def neighbours(a, i, j):
    b = []
    length = len(a)
    if i - 1 >= 0:
        b.append(a[i - 1][j])
        if j - 1 >= 0:
            b.append(a[i - 1][j - 1])
        if j + 1 < length:
            b.append(a[i - 1][j + 1])
    if i + 1 < length:
        b.append(a[i + 1][j])
        if j - 1 >= 0:
            b.append(a[i + 1][j - 1])
        if j + 1 < length:
            b.append(a[i + 1][j + 1])
    if j - 1 >= 0:
        b.append(a[i][j - 1])
    if j + 1 < length:
        b.append(a[i][j + 1])
    return b


def countLocalMin(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] < min(neighbours(a, i, j)):
                count += 1
    return count


def specialSum(a):
    result = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i < j:
                result += abs(a[i][j])
    return result


def main():
    n = 5
    matrix = setMatrix(n)
    printMatrix(matrix)
    print("Количество локальных минимумов = ", countLocalMin(matrix))
    print("Сумма модулей элементов, расположенных выше главной диагонали = ", specialSum(matrix))


if __name__ == '__main__':
    main()
