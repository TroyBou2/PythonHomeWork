#  Дан список целых чисел. Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.
# Примеры/Тесты:
# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
# Output:  2
# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
# Output:  -1

list1 = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8]
x = int(input("Введите число: "))
count = 0

for i in list1:
    if i == x:
        count += 1
if count == 0:
    print (-1)
else:     
    print(count)