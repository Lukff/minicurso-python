"""
Calculadora
Recebe um número, depois um argumento e outro número e exibe o resultado.
Faz as quatro operações básicas +, -, * e /.
"""

while (True):
    num1 = float(input('Primeiro número: ')) # converter para número
    op = input('Operador: ')
    num2 = float(input('Segundo número: '))

    # checar o operador
    if op == '+':
        print( num1 + num2 )
    elif op == '-':
        print( num1 - num2)
    elif op == '/':
        print( num1 / num2 )
    elif op == '*':
        print( num1 / num2 )
    else:                          # operação desconhecida
        print('Não conheço essa operação: ' + op)

    # sair do programa
    sair = input("Deseja sair? ")
    if (sair == 'sim' or sair == "Sim" or sair == 's' or sair == 'S'):
        break
