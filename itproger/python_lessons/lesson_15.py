# import time
# import datetime as dt # импортируем модуль datetime в переменную dt.
# import datetime as dt, sys, os, platform # импортируем модуль datetime в переменную dt, модуль sys в переменную sys, модуль os в переменную os.
# from math import sqrt as s, ceil # импортируем функцию sqrt из модуля math в переменную s
# import mymodule as my # импортируем модуль mymodule в переменную my
from mymodule import add_three_numbers as add # импортируем функцию add_three_numbers из модуля mymodule в переменную add

print(add(10, 20, 30))
# print(my.name)
# print(ceil(s(25)))
# print(sys.path)
# print(os.name)
# print(platform.system())
# time.sleep(3)
# print(dt.datetime.now().time())