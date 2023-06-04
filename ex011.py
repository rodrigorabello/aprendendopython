n = float(input ('qual a velocidade do seu carro? '))
if n > 80:
    print('Você foi multado!!')
    multa = (n-80) * 10.63
    print('O valor da sua multa é R${:.2f}'.format(multa))
print ('tenha um bom dia!!!!')