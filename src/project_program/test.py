#for n in range(0,20,1):
#print(n)

#n=0
#while n < 20:
#    n+=1
#    print(n)

#soma = sum(range(0,20))
#print(soma)

print('Sequencia de Fibonacci:')
a, b = 1, 2
while a <= 4000000:
 print(a, end=', ')
 a, b = b, a + b
 print()