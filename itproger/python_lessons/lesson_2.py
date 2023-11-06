
# В питон нет строгой типизации данных!
number = 5
space = " "
digit = '4.5678'
digit2 = 4.5678
word = 'Result ='
boolean = True
str_num = '5'

print(word, number)
print(word, boolean)

print(word + space + digit)
print(word + space + str(digit2))

print(word, number + int(str_num))
print(word + space + str(number + int(str_num)))

del number

number = 7
print(word, number)