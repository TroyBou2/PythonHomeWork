#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#*Пример:*
#6 -> 1  4  1
#24 -> 4  16  4
#    60 -> 10  40  10

s = int(input("Введите количество журавликов: "))
if s % 6 == 0:
    a = s / 6
    pet = int (a)
    kat = pet * 4
    ser = pet
    print (f"Петя сделал {pet} , Сережа {ser} , а Катя {kat}")
else:
    print ("Число журавликов должно быть кратно 6( ")