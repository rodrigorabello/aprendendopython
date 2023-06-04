import colorama
from colorama import Fore

# Inicializar colorama
colorama.init()

valor_casa = float(input("Digite o valor da casa: R$ "))
salario_comprador = float(input("Digite o salário do comprador: R$ "))
anos_pagamento = int(input("Digite a quantidade de anos para pagamento: "))

prestacao_maxima = salario_comprador * 0.3
prestacao = valor_casa / (anos_pagamento * 12)

if prestacao <= prestacao_maxima:
    total_pagamento = prestacao * anos_pagamento * 12
    print(Fore.BLUE + "Empréstimo aprovado!")
    print("Valor da prestação mensal: R$", round(prestacao, 2))
    print("Total a ser pago ao final: R$", round(total_pagamento, 2))
else:
    print(Fore.RED + "Empréstimo negado.")

# Restaurar configurações de cor originais
colorama.deinit()

