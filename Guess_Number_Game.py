def dificuldade_facil():
    print("Você escolheu o nível fácil.")
    print("Você terá 10 tentativas para adivinhar o número.")
    return 10

def dificuldade_dificil():
    print("Você escolheu o nível dificil.")
    print("Você terá 5 tentativas para adivinhar o número.")
    return 5

import random
numero_secreto = random.randint(1, 100)

vidas = 0
tentativas = 0
print("Seja bem vindo ao jogo de adivinhação!")
print("Estou pensando em um número entre 1 e 100.")

escolha = input("Selecione a dificuldade do jogo: (Facil ou Dificil)").lower()


if escolha == "facil":
    tentativas = dificuldade_facil()
    vidas = 10
    
elif escolha == "dificil":
    tentativas = dificuldade_dificil()
    vidas = 5
else:
    print("Opção inválida. Por favor, escolha 'Fácil' ou 'Difícil'.")
    exit()

while tentativas > 0:
    print(f"Você ainda tem {tentativas} tentativas.")
    palpite = int(input("Digite o seu palpite: "))

    if palpite < 1 or palpite > 100:
        print("Por favor, escolha um número entre 1 e 100.")
        continue

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    
    elif palpite < numero_secreto:
        print("O número é maior que o seu palpite.")
        
    else:
        print("O número é menor que o seu palpite.")

    tentativas -= 1
