print("||||CALCULADORA EM PYTHON COM FUNÇÕES||||")

# Funções primeiro!
def soma(numero1, numero2):
    somar = numero1 + numero2
    print("Resultado da soma:", somar)

def subtracao(numero1, numero2):
    subtrair = numero1 - numero2
    print("Resultado da subtração:", subtrair)

def divisao(numero1, numero2):
    if numero2 != 0:
        dividir = numero1 / numero2
        print("Resultado da divisão:", dividir)
    else:
        print("Erro: divisão por zero.")

def multiplicacao(numero1, numero2):
    multiplicar = numero1 * numero2
    print("Resultado da multiplicação:", multiplicar)

# Entrada de dados
numero1 = float(input("Insira o primeiro valor: "))
numero2 = float(input("Insira o segundo valor: "))

# Escolha da operação
opcao = input("Escolha o tipo de operação: (+, -, /, *): ")

# Chamada da função correspondente
if opcao == '+':
    soma(numero1, numero2)
elif opcao == '-':
    subtracao(numero1, numero2)
elif opcao == '/':
    divisao(numero1, numero2)
elif opcao == '*':
    multiplicacao(numero1, numero2)
else:
    print("Operação inválida.")

