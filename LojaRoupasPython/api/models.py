from typing import List
from datetime import datetime

class Roupa:
    def __init__(self, id: int, nome: str, preco: float, tamanho: str, usuario: str, data_hora: datetime):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.tamanho = tamanho
        self.usuario = usuario
        self.data_hora = data_hora

# Lista inicial de roupas
roupas: List[Roupa] = [
    Roupa(1, "Camiseta", 49.90, "M", "admin", datetime.now()),
    Roupa(2, "Calça Jeans", 129.90, "42", "admin", datetime.now()),
]
