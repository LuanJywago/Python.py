#Cifra de cesar feito em python com codificador e decodificador:
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def encriptar(texto_original, espaco_usado):
    cipher_text = ""

    for letra in texto_original:
        if letra in alfabeto:
            espacamento_usado = (alfabeto.index(letra) + espaco_usado) % len(alfabeto)
            cipher_text += alfabeto[espacamento_usado]
        else:
            cipher_text += letra

    print(f"Aqui está o resultado da codificação: {cipher_text}")


def descodificar(texto_original, espaco_usado):
    texto_saida = ""

    for letra in texto_original:
        if letra in alfabeto:
            espacamento_usado = (alfabeto.index(letra) - espaco_usado) % len(alfabeto)
            texto_saida += alfabeto[espacamento_usado]
        else:
            texto_saida += letra

    print(f"Aqui está o resultado da decodificação: {texto_saida}")


deseja_continuar = True

while deseja_continuar:
    direcao = input("Digite 'codificar' para encriptar algo ou digite 'descodificar' para descriptar algo\n").lower()
    texto = input("Digite a sua mensagem:\n").lower()
    espaco = int(input("Digite a quantidade de espaço utilizado\n"))

    if direcao == 'codificar':
        encriptar(texto, espaco)
    elif direcao == 'descodificar':
        descodificar(texto, espaco)
    else:
        print("Opção inválida")

    reiniciar = input("Digite sim para continuar ou não para parar.\n").lower()

    if reiniciar == "não":
        deseja_continuar = False
        print("Processo finalizado\n")
    else:
        deseja_continuar = True
        print("Processo contínuo!\n")