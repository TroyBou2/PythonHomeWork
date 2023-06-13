# 7.1[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
# Если ритм есть, функция возвращает True, иначе возвращает False

# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True
# Примечание.

# Подумайте об эффективности алгоритма. Какие структуры данных будут более эффективны по скорости.
# Алгоритм должен работать так, чтобы не делать лишних проверок. Подумайте, возможно некоторые проверки не нужны.
# (*) Усложнение.

# Функция имеет параметр, который определяет, надо ли возвращать полную информацию о кол-ве гласных букв в фразах. 
# Эта информация возвращается в виде списка словарей. Каждый элемент списка(словарь) соответствует фразе.

# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", False) -> True
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", True) -> (True, [{'а': 4}, {'а': 4}, {'а': 4}])
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 1, 'о': 1}])
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> (False, [{'а': 4}, {'а': 2, 'у': 3}])
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> (False, [{'а': 11}, {'у': 6, 'а': 3}])
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])

# vinni_song = ("пара-ра-рам рам-пуум-пупам па-ре-по-дам").lower().split()
# vowels = "а,о,э,е,и,ы,у,ё,ю,я"
# print (vinni_song)
# def search_vowels (vinni_song):
#     count = 0
#     for i in vinni_song:
#         for j in i:
#             if j in vowels:
#                 count += 1
#     if count % 2 == 0:
#         return True
#     else:
#         return False
    
# print (search_vowels(vinni_song))

vinni_song = ("пара-ра-рам рам-пум-пупам па-ре-по-дам").lower().split()
vinni_song_1 = ("пара-ра-рам рам-пуум-пупам па-ре-по-дам").lower().split()
vowels = ["а","о","э","е","и","ы","у","ё","ю","я"]

def search_vowels (vinni_song, return_counts = False):
    result = []
    for i in vinni_song:
        count = 0
        for j in i:
            if j in vowels:
                count += 1
        result.append({"фраза": i, "гласных": count})
    if return_counts:
        return result
    else:
        total_count = sum([r["гласных"] for r in result])
        return total_count % 2 == 0
    
                            #Тесты

print (search_vowels(vinni_song))
print (search_vowels (vinni_song, return_counts = True))

print (search_vowels(vinni_song_1))
print (search_vowels (vinni_song_1, return_counts = True))