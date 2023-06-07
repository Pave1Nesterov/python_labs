class Route:
    def __init__(self, dep, arr, num):
        self.departure_point = dep
        self.arrival_point = arr
        self.route_number = num


def show_menu():
    print("\nМеню")
    print("1. Создать записи")
    print("2. Поиск записи по номеру маршрута")
    print("3. Запись данных в файл")
    print("4. Считать данные из файла")
    print("5. Выход из программы")
    while True:
        choice = int(input("Выберите действие: "))
        if 1 <= choice <= 5:
            break
    return choice


def add_routes():
    records = []
    while True:
        n = int(input("Количество записей: "))
        if n > 0:
            break
    for i in range(n):
        print(f"Запись {i + 1}")
        while True:
            dep_point = input("Введите начальный пункт маршрута: ")
            if dep_point != "":
                break
            else:
                print("ОШИБКА! Начальный пункт не введён")
        while True:
            arr_point = input("Введите конечный пункт маршрута: ")
            if arr_point != "":
                break
            else:
                print("ОШИБКА! Конечный пункт не введён")
        route_num = int(input("Введите номер маршрута: "))
        records.append(Route(dep_point, arr_point, route_num))
    records = sorted(records, key=lambda route: route.route_number)
    return records


def find_route(records):
    route_num = int(input("\nВведите номер маршрута: "))
    route = []
    for i in range(len(records)):
        if records[i].route_number == route_num:
            print(f"Запись маршрута под номером {route_num}:")
            route.append(f"{records[i].departure_point} {records[i].arrival_point} {records[i].route_number}")
    if len(route) > 0:
        for i in range(len(route)):
            print(route[i])
    else:
        print(f"Запись с номером маршрута {route_num} не найдена")


def write_routes(records):
    file_name = input("\nВведите имя файла: ")
    f = open(f"{file_name}", "w", encoding="utf-8")
    for i in range(len(records)):
        f.write(f"{records[i].departure_point} {records[i].arrival_point} {records[i].route_number}")
        if i != len(records) - 1:
            f.write("\n")
    f.close()
    print("Данные записаны")


def read_file():
    file_name = input("\nВведите имя файла: ")
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                print(line, end="")
        print()
    except FileNotFoundError:
        print("ОШИБКА! Файл с таким именем не найден")


def main():
    routes = add_routes()
    while True:
        move = show_menu()
        if move == 1:
            routes = add_routes()
        elif move == 2:
            find_route(routes)
        elif move == 3:
            write_routes(routes)
        elif move == 4:
            read_file()
        elif move == 5:
            return 0


if __name__ == '__main__':
    main()
