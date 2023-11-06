# # nums = [5, 7, 2, 4, 7, True, 'Hello', 6.7, [5, 7]]

# # nums[0] = 50
# # nums[5] = 1

# # print(nums[8])
# # print(nums[-1])
# # print(nums[-1][1])

# numbers = [5, 6, 7]

# numbers.append(4)
# numbers.append(True)
# numbers.insert(1, False)

# add = [1, 2, 3]
# numbers.extend(add)

# numbers.sort()

# # numbers.pop()
# # numbers.pop(1)
# # numbers.remove(6)
# # numbers.clear()

# # print(numbers.count(5))
# print(len(numbers))

# nums = [5, 2, 7, '50', False]

# for el in nums:
#     el *= 2
#     print(el)

n = int(input('Enter lenght: '))

userList = []

i = 0
while i < n:
    string = 'Enter element #' + str(i + 1) + ': '
    userList.append(input(string))
    i += 1
4
print(userList)