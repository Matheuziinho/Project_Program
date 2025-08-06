#A palindromic number reads the same both ways. The largest palindrome made from the product of
#two digit numbers is 9009 = 91*99.
#Find the largest palindrome made from the product of two digit numbers.


def string_inversa(n):
 return str(n)[::-1]

def max_palindromo(numero_digito):

    max_pal = 0
    num1 = 0
    num2 = 0
    for num1 in range(999, 99, -1):
        for num2 in range(999, 99, -1):
            produto = num1 * num2
            if str(produto) == string_inversa(produto):
                num1 += 1
                num2 += 1
                max_pal = max(max_pal, produto)
    return max_pal
print(f'O maior palíndromo é: {max_palindromo(3)}')