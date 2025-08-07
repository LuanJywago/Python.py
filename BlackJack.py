import random

def distribuir_cartas():
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    cartas = random.choices(cartas)
    return cartas

mao_jogador = []
mao_computador = []

for _ in range(2):
    mao_jogador.append(distribuir_cartas())
    mao_computador.append(distribuir_cartas())
    
def calculate_score():
    