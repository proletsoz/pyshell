# try: # Обработка ошибок
#     x = int(input('Введите число: '))
#     x += 5
#     print(x)
# except ValueError:
#     print('Необходимо ввести число!')

# x = 0
# while x == 0:
#     try:
#         x = int(input('Введите число: '))
#         x += 5
#         print(x)
#     except ValueError:
#         print('Необходимо ввести число!')

try:
    x = 5 / 1
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except ValueError:
    print('Необходимо ввести число!')
else:
    print('Результат:', x)
finally:
    print('Конец программы')

