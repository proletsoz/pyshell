# Множества
data = set('hello') # множество
print(data)
data = {5, 7, 8, 5, 7} # множество
print(data)
data.add(10) # добавление
print(data)
data.remove(10) # удаление
print(data)
data.pop() # удаление последнего
print(data)
data.clear() # очистка
print(data)

nums = [5, 7, 8, 5, 7] # множество
nums_set = set(nums) # преобразование в множество
print(nums_set)


new_data = frozenset([5, 7, 4, '32', True, 4, 5, 7, 8, 5, 7]) # множество
print(new_data)