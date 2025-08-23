from fastapi import FastAPI
from .routes import bp as roupas_bp

app = FastAPI(
    title="Loja de Roupas API",
    description="API para gerenciar roupas",
    version="1.0.0"
)

app.include_router(roupas_bp)
