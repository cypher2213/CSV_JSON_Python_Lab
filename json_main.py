import json
import os


MAIN_FILE = "students.json"
RESULT_FILE = "result.json"



def init_data():
    if os.path.exists(MAIN_FILE):
        return

    data = [
        {"surname": "Іванов", "name": "Олег", "address": "вул. Шевченка 10", "school": 8, "day": "субота", "grade": 7},
        {"surname": "Петренко", "name": "Марія", "address": "вул. Лесі 5", "school": 12, "day": "неділя", "grade": 8},
        {"surname": "Коваль", "name": "Ірина", "address": "вул. Франка 2", "school": 5, "day": "субота", "grade": 7},
        {"surname": "Мельник", "name": "Андрій", "address": "вул. Миру 44", "school": 9, "day": "субота", "grade": 9},
        {"surname": "Мороз", "name": "Сергій", "address": "вул. Садова 12", "school": 6, "day": "неділя", "grade": 8},
        {"surname": "Муха", "name": "Анна", "address": "вул. Київська 99", "school": 8, "day": "субота", "grade": 7},
        {"surname": "Мазур", "name": "Юрій", "address": "вул. Гоголя 1", "school": 3, "day": "неділя", "grade": 7},
        {"surname": "Сокіл", "name": "Олег", "address": "вул. Пушкіна 7", "school": 4, "day": "субота", "grade": 8},
        {"surname": "Ткач", "name": "Аліна", "address": "вул. Лугова 8", "school": 11, "day": "неділя", "grade": 7},
        {"surname": "Федоренко", "name": "Олена", "address": "вул. Квіткова 3", "school": 2, "day": "субота", "grade": 8},
    ]

    with open(MAIN_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



def load_data():
    try:
        with open(MAIN_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл не знайдено!")
        return []
    except json.JSONDecodeError:
        print("Помилка читання JSON!")
        return []


def save_data(data):
    with open(MAIN_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



def show_file():
    data = load_data()
    for item in data:
        print(item)


def add_record():
    data = load_data()
    print("Введіть дані учня:")
    new_item = {
        "surname": input("Прізвище: "),
        "name": input("Ім'я: "),
        "address": input("Адреса: "),
        "school": int(input("Номер школи: ")),
        "day": input("День відвідування (субота/неділя): "),
        "grade": int(input("Клас (7-11): "))
    }
    data.append(new_item)
    save_data(data)
    print("Запис додано!")


def delete_record():
    data = load_data()
    surname = input("Введіть прізвище для видалення: ")

    new_data = [item for item in data if item["surname"] != surname]

    if len(new_data) == len(data):
        print("Запис не знайдено.")
    else:
        save_data(new_data)
        print("Запис видалено.")


def search():
    data = load_data()
    print("Поля: surname, name, address, school, day, grade")
    field = input("Виберіть поле: ")

    if field not in ["surname", "name", "address", "school", "day", "grade"]:
        print("Невірне поле!")
        return

    value = input("Введіть значення: ")
    if field in ["school", "grade"]:
        value = int(value)

    results = [item for item in data if item[field] == value]

    print("Результат пошуку:")
    for r in results:
        print(r)


def solve_task():

    data = load_data()

    result = [
        {
            "surname": item["surname"],
            "name": item["name"],
            "address": item["address"]
        }
        for item in data
        if item["grade"] in [7, 8] and item["day"] == "субота"
    ]

    with open(RESULT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print("Результат записано у", RESULT_FILE)


def menu():
    init_data()

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Показати JSON файл")
        print("2. Додати запис")
        print("3. Видалити запис")
        print("4. Пошук")
        print("5. Виконати завдання варіанта")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            show_file()
        elif choice == "2":
            add_record()
        elif choice == "3":
            delete_record()
        elif choice == "4":
            search()
        elif choice == "5":
            solve_task()
        elif choice == "0":
            break
        else:
            print("Невірний вибір!")


menu()
