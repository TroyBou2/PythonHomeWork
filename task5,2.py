# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

a = int (input("Введите первое число: "))
b = int (input ("Введите второе число: "))

def summa (a,b):
    if b == 0 :
        return a
    if a == 0:
        return b
    if b != 0 :
        return  1 + summa (a , b - 1 )
    return a 

print (summa(a, b))