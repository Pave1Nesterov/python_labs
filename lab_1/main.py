# функция создания строки многочлена
def make_polynomial_str(coefficients):
    str_p = ""
    for i in range(len(coefficients)):
        if coefficients[i] != 0:
            if str_p == "":
                if coefficients[i] < 0:
                    str_p += "- "
            else:
                if coefficients[i] < 0:
                    str_p += " - "
                else:
                    str_p += " + "
            if abs(coefficients[i]) != 1:
                str_p += f"{abs(coefficients[i])}"
            if i != len(coefficients) - 1:
                str_p += "x"
            if abs(coefficients[i]) == 1 and i == len(coefficients) - 1:
                str_p += f"{abs(coefficients[i])}"
            if i < len(coefficients) - 2:
                str_p += f"^{len(coefficients) - i - 1}"
    if str_p == "":
        str_p = "0"
    return str_p

# функция ручного создания многочлена когда известна только степень
def make_polynomial_with_degree():
    while True:
        print("Введите степень многочлена: ", end='')
        deg = int(input())
        if deg >= 0:
            str_base_p = ""
            chr_num = 65
            coefficients = []
            for i in range(deg + 1):
                if i != 0:
                    str_base_p += " + "
                str_base_p += f"{chr(chr_num)}"
                if i != deg:
                    str_base_p += "x"
                if i < deg - 1:
                    str_base_p += f"^{deg - i}"
                chr_num += 1
            print("\nСоздание многочлена вида:", str_base_p)
            print("Ввод коэффициентов многочлена:")
            chr_num = 65
            for i in range(deg + 1):
                print(f"{chr(chr_num)} = ", end='')
                coefficients.append(int(input()))
                chr_num += 1
            str_polynomial = make_polynomial_str(coefficients)
            print("Получился многочлен:", str_polynomial)
            return deg, coefficients, str_base_p, str_polynomial

# функция автоматического создания с уже известными коэффициентами
def make_with_coefficients(deg, coefs):
    degree = deg
    coefficients = coefs
    str_base_p = ""
    chr_num = 65
    for i in range(deg + 1):
        if i != 0:
            str_base_p += " + "
        str_base_p += f"{chr(chr_num)}"
        if i != deg:
            str_base_p += "x"
        if i < deg - 1:
            str_base_p += f"^{deg - i}"
        chr_num += 1
    str_polynomial = make_polynomial_str(coefficients)
    return degree, coefficients, str_base_p, str_polynomial


def remove_polynomial():
    print_polynomials()
    print("Удаление многочлена")
    while True:
        print("№ многочлена: ", end='')
        choice_pol_1 = int(input())
        if 1 <= choice_pol_1 <= len(polynomials):
            polynomials.pop(choice_pol_1 - 1)
            print(f"Многочлен № {choice_pol_1} удалён")
            break
        else:
            print("Ошибка, многочлена с таким номер не существует. Попробуйте ввести номер ещё раз")


def print_polynomials():
    print("\nСписок многочленов:")
    for i in range(len(polynomials)):
        print(f"{i + 1}. {polynomials[i][3]}")


def print_polynomials_description():
    print_polynomials()
    while True:
        print("№ многочлена: ", end='')
        choice_pol_1 = int(input())
        if 1 <= choice_pol_1 <= len(polynomials):
            print("\nОписание многочлена")
            print(f"Многочлен {polynomials[choice_pol_1 - 1][3]}")
            print(f"Стандартный вид: {polynomials[choice_pol_1 - 1][2]}")
            print(f"Степень = {polynomials[choice_pol_1 - 1][0]}")
            print("Коэффициенты:")
            for i in range(len(polynomials[choice_pol_1 - 1][1])):
                print(polynomials[choice_pol_1 - 1][1][i], end=' ')
            break
        else:
            print("Ошибка, многочлена с таким номер не существует. Попробуйте ввести номер ещё раз")


def addition_polynomials():
    coefs_1 = []
    coefs_2 = []
    print("Сложение двух многочленов")
    print_polynomials()
    print("Выберите номера многочленов для сложения:")
    while True:
        print("№ 1-го слагаемого: ", end='')
        choice_pol_1 = int(input())
        if 1 <= choice_pol_1 <= len(polynomials):
            for i in range(len(polynomials[choice_pol_1 - 1][1])):
                coefs_1.append(polynomials[choice_pol_1 - 1][1][i])
            break
        else:
            print("Ошибка, многочлена с таким номер не существует. Попробуйте ввести номер ещё раз")
    while True:
        print("№ 2-го слагаемого: ", end='')
        choice_pol_2 = int(input())
        if 1 <= choice_pol_2 <= len(polynomials):
            for i in range(len(polynomials[choice_pol_2 - 1][1])):
                coefs_2.append(polynomials[choice_pol_2 - 1][1][i])
            break
        else:
            print("Ошибка, многочлена с таким номер не существует. Попробуйте ввести номер ещё раз")
    if len(coefs_1) < len(coefs_2):
        t = coefs_1
        coefs_1 = coefs_2
        coefs_2 = t
    coefs_1 = reverse_array(coefs_1)
    coefs_2 = reverse_array(coefs_2)
    result_coefs = coefs_1
    for i in range(len(coefs_2)):
        result_coefs[i] += coefs_2[i]
    result_coefs = reverse_array(result_coefs)
    sum_polynomial = make_with_coefficients(len(result_coefs) - 1, result_coefs)
    print(f"\nРезультат сложения многочленов:\n({polynomials[choice_pol_1 - 1][3]}) + ({polynomials[choice_pol_2 - 1][3]}) = {sum_polynomial[3]}")
    return sum_polynomial


def subtraction_polynomials():
    coefs_1 = []
    coefs_2 = []
    print("Разность двух многочленов")
    print_polynomials()
    print("Выберите номера многочленов для вычитания:")
    while True:
        print("№ уменьшаемого: ", end='')
        choice_pol_1 = int(input())
        if 1 <= choice_pol_1 <= len(polynomials):
            for i in range(len(polynomials[choice_pol_1 - 1][1])):
                coefs_1.append(polynomials[choice_pol_1 - 1][1][i])
            break
        else:
            print("Ошибка, многочлена с таким номер не существует. Попробуйте ввести номер ещё раз")
    while True:
        print("№ вычитаемого: ", end='')
        choice_pol_2 = int(input())
        if 1 <= choice_pol_2 <= len(polynomials):
            for i in range(len(polynomials[choice_pol_2 - 1][1])):
                coefs_2.append(polynomials[choice_pol_2 - 1][1][i])
            break
        else:
            print("Ошибка, многочлена с таким номер не существует. Попробуйте ввести номер ещё раз")
    coefs_1 = reverse_array(coefs_1)
    coefs_2 = reverse_array(coefs_2)
    result_coefs = []
    if len(coefs_1) < len(coefs_2):
        for i in range(len(coefs_2)):
            result_coefs.append(coefs_2[i] * (-1))
        for i in range(len(coefs_1)):
            result_coefs[i] += coefs_1[i]
    else:
        result_coefs = coefs_1
        for i in range(len(coefs_2)):
            result_coefs[i] -= coefs_2[i]
    result_coefs = reverse_array(result_coefs)
    sub_polynomial = make_with_coefficients(len(result_coefs) - 1, result_coefs)
    print(f"\nРезультат разности многочленов:\n({polynomials[choice_pol_1 - 1][3]}) - ({polynomials[choice_pol_2 - 1][3]}) = {sub_polynomial[3]}")
    return sub_polynomial


def multiplication_polynomials():
    coefs_1 = []
    coefs_2 = []
    print("Произведение двух многочленов")
    print_polynomials()
    print("Выберите номера многочленов для умножения:")
    while True:
        print("№ 1-го множителя: ", end='')
        choice_pol_1 = int(input())
        if 1 <= choice_pol_1 <= len(polynomials):
            for i in range(len(polynomials[choice_pol_1 - 1][1])):
                coefs_1.append(polynomials[choice_pol_1 - 1][1][i])
            break
        else:
            print("Ошибка, многочлена с таким номер не существует. Попробуйте ввести номер ещё раз")
    while True:
        print("№ 2-го множителя: ", end='')
        choice_pol_2 = int(input())
        if 1 <= choice_pol_2 <= len(polynomials):
            for i in range(len(polynomials[choice_pol_2 - 1][1])):
                coefs_2.append(polynomials[choice_pol_2 - 1][1][i])
            break
        else:
            print("Ошибка, многочлена с таким номер не существует. Попробуйте ввести номер ещё раз")
    if len(coefs_1) < len(coefs_2):
        t = coefs_1
        coefs_1 = coefs_2
        coefs_2 = t
    coefs_1 = reverse_array(coefs_1)
    coefs_2 = reverse_array(coefs_2)
    result_degree = len(coefs_1) + len(coefs_2) - 1
    result_coefs = [0] * result_degree
    for i in range(len(coefs_1)):
        for j in range(len(coefs_2)):
            result_coefs[i + j] += (coefs_1[i] * coefs_2[j])
    result_coefs = reverse_array(result_coefs)
    mul_polynomial = make_with_coefficients(result_degree - 1, result_coefs)
    print(f"\nРезультат произведения многочленов:\n({polynomials[choice_pol_1 - 1][3]}) * ({polynomials[choice_pol_2 - 1][3]}) = {mul_polynomial[3]}")
    return mul_polynomial

def calculate_polynomial_value():
    coefs_1 = []
    result = 0
    print("Вычисление значения многочлена для заданного аргумента")
    print_polynomials()
    while True:
        print("№ многочлена: ", end='')
        choice_pol_1 = int(input())
        if 1 <= choice_pol_1 <= len(polynomials):
            for i in range(len(polynomials[choice_pol_1 - 1][1])):
                coefs_1.append(polynomials[choice_pol_1 - 1][1][i])
            break
        else:
            print("Ошибка, многочлена с таким номер не существует. Попробуйте ввести номер ещё раз")
    print("Введите значение x: ", end='')
    value = int(input())
    result_degree = len(coefs_1) - 1
    for i in range(result_degree + 1):
        result += coefs_1[i] * (value ** (result_degree - i))
    return result


def multiplication_by_constant():
    coefs_1 = []
    print("Умножение многочлена на константу")
    print_polynomials()
    print("Выберите номер многочлена для умножения:")
    while True:
        print("№: ", end='')
        choice_pol_1 = int(input())
        if 1 <= choice_pol_1 <= len(polynomials):
            for i in range(len(polynomials[choice_pol_1 - 1][1])):
                coefs_1.append(polynomials[choice_pol_1 - 1][1][i])
            break
        else:
            print("Ошибка, многочлена с таким номер не существует. Попробуйте ввести номер ещё раз")
    print("Введите значение константы: ", end='')
    value = int(input())
    for i in range(len(coefs_1)):
        coefs_1[i] *= value
    mul_polynomial = make_with_coefficients(len(coefs_1) - 1, coefs_1)
    print(f"\nРезультат умножения многочлена на константу:\n({polynomials[choice_pol_1 - 1][3]}) * ({value}) = {mul_polynomial[3]}")
    return mul_polynomial


def derivative_polynomial():
    coefs_1 = []
    print("Вычисление производной")
    print_polynomials()
    print("Выберите номер многочлена для вычисления производной: ")
    while True:
        print("№: ", end='')
        choice_pol_1 = int(input())
        if 1 <= choice_pol_1 <= len(polynomials):
            for i in range(len(polynomials[choice_pol_1 - 1][1])):
                coefs_1.append(polynomials[choice_pol_1 - 1][1][i])
            break
        else:
            print("Ошибка, многочлена с таким номер не существует. Попробуйте ввести номер ещё раз")
    current_degree = len(coefs_1) - 1
    result_degree = current_degree - 1
    result_coefs = []
    for i in range(current_degree):
        result_coefs.append(coefs_1[i] * current_degree)
        current_degree -= 1
        i -= 1
    der_polynomial = make_with_coefficients(result_degree, result_coefs)
    print(f"\nРезультат вычисления производной:\n({polynomials[choice_pol_1 - 1][3]})' = {der_polynomial[3]}")
    return der_polynomial


def reverse_array(arr):
    a = arr
    n = len(a)
    for i in range(n // 2):
        j = n - i - 1
        t = a[i]
        a[i] = a[j]
        a[j] = t
    return a


polynomials = []


while True:
    print("\nВыберите действие:")
    print("1. Создать многочлен")
    print("2. Удалить многочлен из списка")
    print("3. Вывести список многочленов")
    print("4. Вывести описание многочлена")
    print("5. Вычислить сумму двух многочленов")
    print("6. Вычислить разность двух многочленов")
    print("7. Вычислить произведение двух многочленов")
    print("8. Вычислить значение многочлена при заданной переменной x")
    print("9. Вычислить произведение многочлена на константу")
    print("10. Вычислить производную многочлена")
    print("0. Выйти из программы")

    print("Введите номер действия: ", end='')
    choice = int(input())

    if choice == 1:
        polynomial = make_polynomial_with_degree()
        polynomials.append(polynomial)
    elif choice in [2, 3, 4, 8]:
        if len(polynomials) == 0:
            print("Список многочленов пуст")
        else:
            if choice == 2:
                remove_polynomial()
            elif choice == 3:
                print_polynomials()
            elif choice == 4:
                print_polynomials_description()
            else:
                print(f"Результат: {calculate_polynomial_value()}")
    elif choice in [5, 6, 7, 9, 10]:
        if len(polynomials) == 0:
            print("Недостаточно многочленов для выполнения операции")
        else:
            if choice == 5:
                polynomial = addition_polynomials()
            elif choice == 6:
                polynomial = subtraction_polynomials()
            elif choice == 7:
                polynomial = multiplication_polynomials()
            elif choice == 9:
                polynomial = multiplication_by_constant()
            else:
                polynomial = derivative_polynomial()
            while True:
                print("        Добавить получившийся многочлен в список многочленов?")
                print("        1. Да")
                print("        2. Нет")
                print("        Введите номер действия: ", end='')
                choice_add_pol = int(input())
                if choice_add_pol == 1:
                    polynomials.append(polynomial)
                    print("        Многочлен добавлен")
                    break
                elif choice_add_pol == 2:
                    print("        Многочлен не добавлен")
                    break
                else:
                    print("        Неверный выбор действия. Попробуйте еще раз.")
    elif choice == 0:
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор действия. Попробуйте еще раз.")
