# Кортежи имеют меньше памяти, чем списки, но могут содержать любые типы данных

data = (4, 6, 7, 3, 6, True, 5.6 , 'Hello') # кортеж
# # data[0] = 10 - not possible
# print(data[1:5]) # срез
# print(data.count(6)) # подсчет количества элементов
# print(len(data)) # длина кортежа
# print(data) # вывод кортежа

# data = 5, 7, True # кортеж без скобок
# data = (5,) # кортеж с одним элементом

for el in data: # перебор
    print(el)

nums = [5, 7, 8] # список
new_data = tuple(nums) # преобразование в кортеж
print(new_data)

word = tuple('Hello') # преобразование строки в кортеж
print(word)