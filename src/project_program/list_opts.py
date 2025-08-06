#lists in python
from functools import reduce


list1 = [1, 2, 3, 4, 5]
print(list1)

list2 = ['a', 'b', 'c', 'd', 'e']
print(list2)

list3 = ['zé', 'joão', 'maria', 'ana']
print(list3)

print(30 * '-')

#-----------------------------------------------------
def append(list1, list2):
    list1.append(list2)
    return list1
print(append(list1, 6))

#-----------------------------------------------------
def concatenate(list1, list2, list3):
    return list1 + list2 + list3
print(concatenate(list1, list2, list3))

#-----------------------------------------------------
def filter(list1):
   return list(filter(lambda x: x % 2 == 0, list1))

#-----------------------------------------------------
length_list = len(list3)
print(length_list)

#-----------------------------------------------------
mapped_list = list(map(lambda x: x + 2, list1))
print(mapped_list)

#-----------------------------------------------------
fold_left = reduce(lambda x, y: x + y, list1)
print(fold_left)

#-----------------------------------------------------
fold_right = reduce(lambda x, y: x + y, reversed(list1))
print(fold_right)

#-----------------------------------------------------
reversed_list = list(reversed(list3))
print(reversed_list)
