"""
Calculadora
Recebe um número, depois um argumento e outro número e exibe o resultado.
Faz as quatro operações básicas +, -, * e /.
"""

def calc(num1, num2, op):
    """Retorna o resultado de uma operação em num1 e num2."""
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '/':
        return num1 / num2
    elif op == '*':
        return num1 / num2
    else:           # operação desconhecida
        return None
