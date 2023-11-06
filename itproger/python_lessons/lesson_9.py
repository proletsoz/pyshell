country = {'code': 'RU', 'name': 'Russia', 'population': 145} # словарь
# country = dict(code='RU', name='Russia', population=145) # словарь

# print(country['name']) # ключ
# print(country) # вывод словаря
# print(country.items()) # вывод ключей и значений 

# for key, value in country.items(): # перебор
    # print(key, '--', value) # вывод ключей и значений

# print(country['code']) # ключ
# print(country.get('name')) # ключ
# country.clear() # очистка
# country.pop('name') # удаление
# country.popitem() # удаление последнего
# print(country.keys()) # вывод ключей
# print(country.values()) # вывод значений
# print(country.items()) # вывод ключей и значений
# country.update({'code': 'RU', 'name': 'Russia', 'population': 145}) # обновление
# country['code'] = 'RU' # обновление
# print(country) # вывод словаря

person = { # cловарь
    'user_1': { #
        'name': 'Ivan',
        'surname': 'Ivanov',
        'age': 25,
        'address': ('Moscow', 'Lenina'), # кортеж
        'grades': {'math': 5, 'physics': 5, 'chemistry': 5}, # словарь
        'is_married': True
    },
    'user_2': {
        'name': 'Petr',
        'surname': 'Petrov',
        'age': 30,
        'address': ('Moscow','Lenina'),
        'grades': {'math': 5 , 'physics': 3, 'chemistry': 4},
        'is_married': False
    }
}

print(person['user_1']['grades']['math'])
print(person['user_2'])

