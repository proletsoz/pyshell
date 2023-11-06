try:
    # file = open('text.txt', 'r')
    # file.read()
    with open('text.txt', 'r') as file:
        file.read()
    print('File is found')
except FileNotFoundError:
    print('File not found')
# finally:
#     print('File is cloused')
#     file.close()