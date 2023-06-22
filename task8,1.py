# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller


import csv
phone_book = []

def create_entry():
    second_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    descriptions = input("Введите описание:")
    registration = {
        "Фамилия": second_name,
        "Имя": first_name,
        "Телефон": phone,
        "Описание": descriptions
    }
    phone_book.append(registration)
    print("Новая запись добавлена в телефонную книгу")

def read_entry():
    search_string = input("Введите строку поиска: ")
    for rec in phone_book:
        if search_string in rec["Фамилия"]:
            print (rec)
            break
    else:
        print("Подходящая запись не найдена")

def update_entry():
    search_string = input("Введите строку поиска: ")
    for rec in phone_book:
        if search_string in rec["Фамилия"]:
            rec["Фамилия"] = input("Введите новую фамилию: ")
            rec["Имя"] = input("Введите новое имя: ")
            rec["Телефон"] = input("Введите новый номер телефона: ")
            rec["Описание"] = input("Введите новое описание: ")
            print("Запись обновлена")
            break
    else:
        print("Подходящая запись не найдена")

def delete_entry():
    search_string = input("Введите строку поиска: ")
    for idx, rec in enumerate(phone_book):
        if  search_string in rec["Фамилия"]:
            del(phone_book[idx])
            print("Запись удалена")
            break
    else:
        print("Подходящая запись не найдена")

def export_data():
    with open("phone_book.csv","r", encoding='utf-8') as file :
        reader = csv.DictReader (file)
        for rec in reader:
            phone_book.append(rec)
    print("Данные экспортированы из phone_book.csv")


def import_data():
    with open("phone_book.csv", "w", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Фамилия", "Имя", "Телефон", "Описание"])
        writer.writeheader()
        writer.writerows (phone_book)
    print("Данные импортированы в phone_book.csv")    


while True:
    print("\nВыберите вариант:")
    print("1. Создать запись")
    print("2. Прочитать запись")
    print("3. Обновить запись")
    print("4. Удалить запись")
    print("5. Импорт данных")
    print("6. Экспорт данных")
    print("7. Выход")
    selection = input("Введите свой выбор: ")
    if selection == "1":
        create_entry()
    elif selection == "2":
        read_entry()
    elif selection == "3":
        update_entry()
    elif selection == "4":
        delete_entry()
    elif selection == "5":
        import_data()
    elif selection == "6":
        export_data()
    elif selection == "7":
        break
    else:
        print("Неверный выбор")