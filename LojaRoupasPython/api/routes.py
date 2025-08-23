from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime
from .models import Roupa, roupas

bp = APIRouter()

# Modelo Pydantic para requisições
class RoupaSchema(BaseModel):
    id: int
    nome: str
    preco: float
    tamanho: str
    usuario: str  # usuário que está fazendo a operação

class RoupaResponse(RoupaSchema):
    data_hora: datetime

@bp.get("/roupas", response_model=List[RoupaResponse])
def listar_roupas():
    return roupas

@bp.get("/roupas/{id}", response_model=RoupaResponse)
def buscar_roupa(id: int):
    for r in roupas:
        if r.id == id:
            return r
    raise HTTPException(status_code=404, detail="Roupa não encontrada")

@bp.post("/roupas", response_model=RoupaResponse)
def adicionar_roupa(roupa: RoupaSchema):
    for r in roupas:
        if r.id == roupa.id:
            raise HTTPException(status_code=400, detail="ID já existe")
    nova = Roupa(
        id=roupa.id,
        nome=roupa.nome,
        preco=roupa.preco,
        tamanho=roupa.tamanho,
        usuario=roupa.usuario,
        data_hora=datetime.now()
    )
    roupas.append(nova)
    return nova

@bp.put("/roupas/{id}", response_model=RoupaResponse)
def atualizar_roupa(id: int, dados: RoupaSchema):
    for r in roupas:
        if r.id == id:
            r.nome = dados.nome
            r.preco = dados.preco
            r.tamanho = dados.tamanho
            r.usuario = dados.usuario
            r.data_hora = datetime.now()
            return r
    raise HTTPException(status_code=404, detail="Roupa não encontrada")

@bp.delete("/roupas/{id}")
def remover_roupa(id: int, usuario: str):
    for r in roupas:
        if r.id == id:
            roupas.remove(r)
            return {"detail": f"Roupa removida por {usuario} em {datetime.now()}"}
    raise HTTPException(status_code=404, detail="Roupa não encontrada")
