import random

# Distribui cartas
def distribuir_cartas():
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cartas)

# Calcula a pontuação
def calculate_score(cartas):
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0  # BlackJack
    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)

# Compara as pontuações
def compare(u_score, c_score):
    if u_score == c_score:
        return "Empate!"
    elif c_score == 0:
        return "Computador ganhou com BlackJack!"
    elif u_score == 0:
        return "Você ganhou com BlackJack!"
    elif u_score > 21:
        return "Você perdeu! Sua pontuação é maior que 21."
    elif c_score > 21:
        return "Computador perdeu! Sua pontuação é maior que 21."
    elif u_score > c_score:
        return "Você ganhou!"
    else:
        return "Computador ganhou!"

# Mãos iniciais
mao_jogador = []
mao_computador = []
game_over = False

# Duas cartas para cada
for _ in range(2):
    mao_jogador.append(distribuir_cartas())
    mao_computador.append(distribuir_cartas())

# Loop principal do jogador
while not game_over:
    user_score = calculate_score(mao_jogador)
    computer_score = calculate_score(mao_computador)

    print(f"Suas cartas: {mao_jogador}, sua pontuação: {user_score}")
    print(f"Primeira carta do computador: {mao_computador[0]}")

    # Verifica fim de jogo imediato
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        should_continue = input("Digite 'y' para receber outra carta, ou 'n' para parar: ")
        if should_continue == 'y':
            mao_jogador.append(distribuir_cartas())
        else:
            game_over = True

# Turno do computador
while computer_score != 0 and computer_score < 17:
    mao_computador.append(distribuir_cartas())
    computer_score = calculate_score(mao_computador)

# Exibe resultado final
print("\n--- Resultado Final ---")
print(f"Suas cartas: {mao_jogador}, sua pontuação: {user_score}")
print(f"Cartas do computador: {mao_computador}, pontuação: {computer_score}")
print(compare(user_score, computer_score))
