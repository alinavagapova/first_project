# 4. Создать словарь (не пустой) и отобразить все пары ключ значение
#     если значение равно 'Alina'

# это решение я нашла в интернете
# test_dict = {'key_1': 'Alina', 'key_2': 'notAlina', 'key_3': 'one_more_Alina', 'key_4': 'Alina'}
# alina_dict = test_dict.items()
# for key, values in alina_dict:
#     if values == 'Alina':
#         print(key, '->', values)

test_dict = {'key_1': 'Alina', 'key_2': 'notAlina', 'key_3': 'one_more_Alina', 'key_4': 'Alina'}
for i, j in test_dict.items():
    if j == 'Alina':
        print(i, j)


