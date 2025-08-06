
# Entrada
print('Calcular o maior fator primo de um número')
print('-' * 30)
print('Qual é o número?')


# Variável int para o usuário definir o número
num = int(input())

# Verificar se o número é primo
if num >= 1:
    for i in range(2, num):
        if num % i == 0:
            print('-' * 30)
            print('O', num, 'não é primo.')
            break
        elif num <= 0:
            print('O número deve ser maior que 0')
            break
else:
  print('O', num, 'é primo. Logo, o maior fator primo é ele mesmo.')

#-----------------------------------------------------------------------------------
# Função para calcular os fatores do número
def fatores(num):
    fatores = []
    for i in range(1, num + 1):
        if num % i == 0:
            fatores.append(i)
    return fatores

print('-' * 30)
print('Os fatores de', num, 'são:', fatores(num))
print('-' * 30)

#-----------------------------------------------------------------------------------
#Função para definir o maior fator primo de um número

def maior_fator_primo(num):
    fatores = []
    for i in range(2, num + 1):
        while num % i == 0:
            fatores.append(i)
            num //= i
    return max(fatores) if fatores else None

print('O maior fator primo de', num, 'é:', maior_fator_primo(num))