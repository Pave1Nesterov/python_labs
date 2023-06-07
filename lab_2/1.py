from tkinter import *

single_digits = {
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9
}

tens_digits = {
    'десять': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19
}

two_digits = {
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90
}

three_digits = {
    'сто': 100,
    'двести': 200,
    'триста': 300,
    'четыреста': 400,
    'пятьсот': 500,
    'шестьсот': 600,
    'семьсот': 700,
    'восемьсот': 800,
    'девятьсот': 900
}

roman_digits = {
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}


def check_correctness(string_number):
    result = True
    if len(string_number) == 0:
        label_error.config(text="Число не введено!", fg="red")
        result = False
    else:
        single_d = tens_d = two_d = three_d = 0
        for key in range(len(string_number)):
            if string_number[key] in three_digits:
                three_d += 1
            elif string_number[key] in two_digits:
                two_d += 1
            elif string_number[key] in tens_digits:
                tens_d += 1
            elif string_number[key] in single_digits:
                single_d += 1
            else:
                if len(string_number) == 1 and string_number[0] == "ноль":
                    return result
                elif len(string_number) >= 1:
                    if "ноль" in string_number:
                        label_error.config(
                            text="Ошибка! Слово \"ноль\" не может применяться совместно с другими разрядами".format(
                                key + 1),
                            fg="red",
                            wraplength=300)
                    else:
                        label_error.config(text="Ошибка! Слово \"{}\" введено неверно".format(string_number[key]),
                                           fg="red",
                                           wraplength=300)
                result = False
                return result
            if three_d > 1:
                for i in range(len(string_number) - 1):
                    if string_number[i] in three_digits and string_number[i + 1] in three_digits:
                        label_error.config(text="Ошибка! Разряд сотен используется несколько раз ({}) подряд".format(three_d),
                                           fg="red",
                                           wraplength=300)
                        break
                    else:
                        label_error.config(
                            text="Ошибка! Разряд сотен используется несколько раз ({})".format(three_d),
                            fg="red",
                            wraplength=300)
                result = False
                return result
            elif tens_d > 1:
                for i in range(len(string_number) - 1):
                    if string_number[i] in tens_digits and string_number[i + 1] in tens_digits:
                        label_error.config(text="Ошибка! Числа из промежутка 10-19 используются несколько раз ({}) подряд".format(tens_d),
                                           fg="red",
                                           wraplength=300)
                        break
                    else:
                        label_error.config(
                            text="Ошибка! Числа из промежутка 10-19 используются несколько раз ({})".format(tens_d),
                            fg="red",
                            wraplength=300)
                result = False
                return result
            elif two_d > 1:
                for i in range(len(string_number) - 1):
                    if string_number[i] in two_digits and string_number[i + 1] in two_digits:
                        label_error.config(text="Ошибка! Разряд десятков используется несколько раз ({}) подряд".format(two_d),
                                           fg="red",
                                           wraplength=300)
                        break
                    else:
                        label_error.config(
                            text="Ошибка! Разряд десятков используется несколько раз ({})".format(two_d),
                            fg="red",
                            wraplength=300)
                result = False
                return result
            elif single_d > 1:
                for i in range(len(string_number) - 1):
                    if string_number[i] in single_digits and string_number[i + 1] in single_digits:
                        label_error.config(text="Ошибка! Разряд единиц используется несколько раз ({}) подряд".format(single_d),
                                           fg="red",
                                           wraplength=300)
                        break
                    else:
                        label_error.config(
                            text="Ошибка! Разряд единиц используется несколько раз ({})".format(single_d),
                            fg="red",
                            wraplength=300)
                result = False
                return result
            for key in range(len(string_number) - 1):
                if string_number[key + 1] in three_digits:
                    if string_number[key] in single_digits:
                        label_error.config(
                            text="Ошибка! Число из разряда сотен (\"{0}\") не может идти после числа из разряда "
                                 "единиц (\"{1}\")".format(string_number[key + 1], string_number[key]),
                            fg="red",
                            wraplength=300)
                    if string_number[key] in tens_digits:
                        label_error.config(
                            text="Ошибка! Число из разряда сотен (\"{0}\") не может идти после числа из промежутка "
                                 "10-19 (\"{1}\")".format(string_number[key + 1], string_number[key]),
                            fg="red",
                            wraplength=300)
                    if string_number[key] in two_digits:
                        label_error.config(
                            text="Ошибка! Число из разряда сотен (\"{0}\") не может идти после числа из разряда "
                                 "десятков (\"{1}\")".format(string_number[key + 1], string_number[key]),
                            fg="red",
                            wraplength=300)
                        result = False
                    break
                if string_number[key + 1] != "":
                    if string_number[key] in single_digits:
                        if string_number[key + 1] in tens_digits:
                            label_error.config(
                                text="Ошибка! После числа из разряда единиц (\"{0}\") не может идти число "
                                     "из промежутка 10-19 (\"{1}\")".format(string_number[key], string_number[key + 1]),
                                fg="red",
                                wraplength=300)
                        if string_number[key + 1] in two_digits:
                            label_error.config(
                                text="Ошибка! После числа из разряда единиц (\"{0}\") не может идти число из разряда "
                                     "десятков (\"{1}\")".format(string_number[key], string_number[key + 1]),
                                fg="red",
                                wraplength=300)
                        result = False
                    elif string_number[key] in tens_digits:
                        if string_number[key + 1] in single_digits:
                            label_error.config(
                                text="Ошибка! После числа из промежутка 10-19 (\"{0}\") не может идти число из разряда "
                                     "единиц (\"{1}\")".format(string_number[key], string_number[key + 1]),
                                fg="red",
                                wraplength=300)
                        if string_number[key + 1] in two_digits:
                            label_error.config(
                                text="Ошибка! После числа из промежутка 10-19 (\"{0}\") не может идти число из разряда "
                                     "десятков (\"{1}\")".format(string_number[key], string_number[key + 1]),
                                fg="red",
                                wraplength=300)
                        result = False
                    if string_number[key] in two_digits and string_number[key + 1] in tens_digits:
                        label_error.config(
                            text="Ошибка! После числа из разряда десятков (\"{0}\") не может идти число из промежутка "
                                 "10-19 (\"{1}\")".format(string_number[key], string_number[key + 1]),
                            fg="red",
                            wraplength=300)
                        result = False
    return result


def make_arabic_number(string_number):
    result = 0

    for i in range(len(string_number)):
        if string_number[i] in three_digits:
            result += three_digits[string_number[i]]
        elif string_number[i] in two_digits:
            result += two_digits[string_number[i]]
        elif string_number[i] in tens_digits:
            result += tens_digits[string_number[i]]
        else:
            if string_number[i] == "ноль":
                return result
            result += single_digits[string_number[i]]
    return result


def make_roman_number(number):
    result = ""
    for key in roman_digits.keys():
        while number >= key:
            result += roman_digits[key]
            number -= key
    return result


def button_click():
    number_str = textBox.get()
    number_str = number_str.lower().split()
    if check_correctness(number_str):
        label_2.config(text="Запись числа арабскими цифрами: " + str(make_arabic_number(number_str)))
        label_3.config(
            text="Запись числа римскими цифрами: " + str(make_roman_number(make_arabic_number(number_str))))
        label_error.config(text="Успешно!", fg="green")


root = Tk()
root.title("Перевод числа из строчного формата в десятичный")
w, h = 500, 450
root.geometry(f"{w}x{h}+{(root.winfo_screenwidth() - w) // 2}+{(root.winfo_screenheight() - h) // 2}")
root.resizable(False, False)

label_1 = Label(root, text="Строковая запись числа: ", font=20)
label_1.pack(anchor="nw", padx=40, pady=(40, 0))
textBox = Entry(root, width=40, font=14)
textBox.pack(anchor="nw", padx=40, pady=10)
label_2 = Label(root, text="Запись числа арабскими цифрами: ", font=20)
label_2.pack(anchor="nw", padx=40, pady=10)
label_3 = Label(root, text="Запись числа римскими цифрами: ", font=20)
label_3.pack(anchor="nw", padx=40, pady=10)
label_4 = Label(root, text="Статус:", font=20)
label_4.pack(anchor="nw", padx=40, pady=(40, 0))
label_error = Label(root, font=20, fg="red", width=400)
label_error.pack(anchor="nw", padx=40, pady=5)
button_translate = Button(root,
                          text="Перевести",
                          width=20,
                          height=1,
                          font=26,
                          command=button_click)
button_translate.pack(side=BOTTOM, pady=15)
root.mainloop()
