n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = float(n1 + n2)
s1 = n1 - n2
s2 = n1 * n2
s3 = n1 / n2
s4 = n1 ** n2
s5 = n1 // n2
s6 = n1 % n2
float(s6)
print(s6)
print('O resultado da soma é:{}'.format(s))
print('O resultado da subtração é {}'.format(s1))
print('O resultado da multiplicação é: {}'.format(s2))
print('O resultado da divisão é: {:.6f}'.format(s3))
print('O resultado da potência de {} elevado a {} é {}, e o resultado da divisão inteira é {} se tiver resto é {}'.format(n1, n2, s4, s5, s6))
