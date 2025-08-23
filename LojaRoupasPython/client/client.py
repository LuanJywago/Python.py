import requests

BASE_URL = "http://127.0.0.1:8000"

def listar_roupas():
    res = requests.get(f"{BASE_URL}/roupas")
    for r in res.json():
        print(f"ID: {r['id']}, Nome: {r['nome']}, Preço: R${r['preco']:.2f}, Tamanho: {r['tamanho']}, Usuário: {r['usuario']}, Data/Hora: {r['data_hora']}")

def buscar_roupa():
    id = int(input("Digite o ID da roupa: "))
    res = requests.get(f"{BASE_URL}/roupas/{id}")
    if res.status_code == 200:
        r = res.json()
        print(f"ID: {r['id']}, Nome: {r['nome']}, Preço: R${r['preco']:.2f}, Tamanho: {r['tamanho']}, Usuário: {r['usuario']}, Data/Hora: {r['data_hora']}")
    else:
        print(res.json()["detail"])

def adicionar_roupa():
    id = int(input("ID: "))
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    tamanho = input("Tamanho: ")
    usuario = input("Usuário: ")
    res = requests.post(f"{BASE_URL}/roupas", json={
        "id": id, "nome": nome, "preco": preco, "tamanho": tamanho, "usuario": usuario
    })
    print(res.json())

def atualizar_roupa():
    id = int(input("ID da roupa que quer atualizar: "))
    nome = input("Novo nome: ")
    preco = float(input("Novo preço: "))
    tamanho = input("Novo tamanho: ")
    usuario = input("Usuário que está atualizando: ")
    res = requests.put(f"{BASE_URL}/roupas/{id}", json={
        "id": id, "nome": nome, "preco": preco, "tamanho": tamanho, "usuario": usuario
    })
    print(res.json())

def remover_roupa():
    id = int(input("ID da roupa que quer remover: "))
    usuario = input("Usuário que está removendo: ")
    res = requests.delete(f"{BASE_URL}/roupas/{id}?usuario={usuario}")
    print(res.json())

def menu():
    while True:
        print("\n=== Menu Loja de Roupas ===")
        print("1 - Listar roupas")
        print("2 - Buscar roupa por ID")
        print("3 - Adicionar roupa")
        print("4 - Atualizar roupa")
        print("5 - Remover roupa")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            listar_roupas()
        elif escolha == "2":
            buscar_roupa()
        elif escolha == "3":
            adicionar_roupa()
        elif escolha == "4":
            atualizar_roupa()
        elif escolha == "5":
            remover_roupa()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
