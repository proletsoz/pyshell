file = open('text.txt', 'w') 

# 'w' - write # 'a' - append
# file.write('Hello world\n')
# file.write('!!!')

data = ''
while data != 'Stop':
    file.write(data + '\n')
    data = input('Enter data: ')

file.close()

file = open('text.txt', 'r') # 'r' - read

# print(file.read())
for line in file:
    print(line, end='')

file.close()