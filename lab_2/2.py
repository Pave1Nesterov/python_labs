import tkinter
from tkinter import *


def button_clear_click():
    entry_text.delete(0, END)
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    label_result.config(text="")
    label_error.config(text="")


def button_move_click():
    label_result.config(text="")
    label_error.config(text="")
    words = entry_text.get().split()
    left_border = str(entry_1.get()).replace(" ", "")
    right_border = str(entry_2.get()).replace(" ", "")
    if not left_border.isdigit():
        label_error.config(text="Ошибка! Левая граница должна быть числом", fg="red")
    elif not right_border.isdigit():
        label_error.config(text="Ошибка! Левая граница должна быть числом", fg="red")
    else:
        left_border = int(left_border)
        right_border = int(right_border)
    start = 1
    finish = len(words)
    if finish == 0:
        label_error.config(text="Ошибка! Не введено ни одного слова", fg="red")
    elif finish == 1:
        label_error.config(text="Ошибка! Для перестановки требуется минимум 2 слова", fg="red")
    else:
        if left_border == "":
            label_error.config(text="Ошибка! Введите начало диапазона", fg="red")
        elif right_border == "":
            label_error.config(text="Ошибка! Введите конец диапазона", fg="red")
        else:
            if left_border <= 0 or right_border <= 0:
                label_error.config(text="Ошибка! Индексация слов начинается с единицы", fg="red")
            else:
                if left_border < start or left_border > finish:
                    label_error.config(text="Ошибка! Левая граница вне диапазона", fg="red")
                elif right_border < start or right_border > finish:
                    label_error.config(text="Ошибка! Правая граница вне диапазона", fg="red")
                elif right_border < left_border:
                    label_error.config(text="Ошибка! Левая граница больше правой", fg="red")
                else:
                    index = right_border - 1
                    while right_border >= left_border:
                        words.insert(0, words[index])
                        words.pop(index + 1)
                        right_border -= 1
                    result_str = words
                    label_result.config(text=result_str)
                    label_error.config(text="Успешно!", fg="green")


root = Tk()
root.title("Перестановка слов из выбранного диапазона в начало строки")
w, h = 800, 450
root.geometry(f"{w}x{h}+{(root.winfo_screenwidth() - w) // 2}+{(root.winfo_screenheight() - h) // 2}")
root.resizable(False, False)

Label(root, text="Введите строку", font=20).grid(row=0, column=0, padx=10, pady=(40, 0), sticky=W)
entry_text = Entry(root, width=45, font=14)
entry_text.grid(row=0, column=1, columnspan=5, pady=(40, 0))
Label(root, text="Диапазон слов от", font=20).grid(row=1, column=0, padx=10, pady=(40, 0))
entry_1 = Entry(root, width=10, font=14)
entry_1.grid(row=1, column=1, pady=(40, 0))
Label(root, text="до", font=20).grid(row=1, column=2, pady=(40, 0))
entry_2 = Entry(root, width=10, font=14)
entry_2.grid(row=1, column=3, pady=(40, 0))
Label(root, text="Результат: ", font=20).grid(row=2, column=0, padx=10, pady=(40, 0), sticky=W)
Label(root, text="Статус: ", font=20).grid(row=3, column=0, padx=10, pady=(40, 0), sticky=W)
label_result = Label(root, font=20)
label_result.grid(row=2, column=1, columnspan=5, pady=(40, 0), sticky=W)
Button(root, text="Очистка", font=20, width=20, height=3, command=button_clear_click)\
    .grid(row=4, column=0, columnspan=3, padx=10, pady=(60, 0))
Button(root, text="Перестановка", font=20, width=20, height=3, command=button_move_click)\
    .grid(row=4, column=3, columnspan=3, padx=10, pady=(60, 0))
label_error = Label(root, text="", font=20)
label_error.grid(row=3, column=1, columnspan=6, pady=(40, 0), sticky=W)

root.mainloop()
