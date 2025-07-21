lances = {}

while True:
    name = input("Informe seu nome: ")
    bid_price = float(input("Informe o valor da sua oferta: R$ "))

    lances[name] = bid_price

    continuar = input("Mais alguem vai fazer alguma oferta? digite (S/N): ").lower()
    if continuar != 's':
        break

print("\nLances registrados nessa rodada: ")
for name, bid_price in lances.items():
    print(f"{name}: R$ {bid_price:.2f}")

vencedor = max(lances, key=lances.get)
print("\n" * 20)
print(f"\nO vencedor foi {vencedor}, com um lance de R$ {lances[vencedor]:.2f}")
