#Задача 2: Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |

num = (input ("Введите трехзначное число:"))
if len(num) == 3:
    num1 = int (num[0])
    num2 = int (num[1])
    num3 = int (num[2])
    sumNum = num1 + num2 + num3
    
    print (f"{num1} + {num2} + {num3} = {sumNum}") 
else: 
    print ("Вы ввели не трёхзначное число!")