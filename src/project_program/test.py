# for n in range(0,20,1):
# print(n)

# n=0
# while n < 20:
#    n+=1
#    print(n)

# soma = sum(range(0,20))
# print(soma)

# print('Sequencia de Fibonacci:')
# a, b = 1, 2
# while a <= 4000000:
# print(a, end=', ')
# a, b = b, a + b
# print()

from functools import reduce

list1 = [1, 2, 3, 4, 5]
# This will return the product of all elements in list1, which is 120
# prod(list1) returns 120, which is the product of 1*2*3*4*5
print(reduce(lambda x, y: x * y, list1))  # Uncomment to see the output
