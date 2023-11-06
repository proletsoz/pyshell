# def testFunction(word):
#     print(word, end='')
#     print('!')
# testFunction('Hi')
# testFunction(5)

# def summa(a, b):
#     return a + b
#     # res = a + b
#     # return res
#     # print('Result:', res)

# print(summa(5, 7))
# print(summa('Hello', 'World'))

# def minimalNumber(l): # [5, 7, 2, 4, 7]
#     minNumInList = l[0] # minNum = 5
#     for el in l: # el = 5
#         if el < minNumInList: # 5 < 5
#             minNumInList = el # minNum = 5
#     print('Minimal number:', minNumInList)

# numbersList1 = [5, 7, 2, 4, 7]
# minimalNumber(numbersList1)
# numbersList2 = [10, 20, 30, 40, 50]
# minimalNumber(numbersList2)

func = lambda x, y: x * y
print(func(5, 7))



