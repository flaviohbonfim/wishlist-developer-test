from fastapi import FastAPI
from .routes import router
from .database import Base, engine

app = FastAPI(
    title="Wishlist API",
    description="API para controle de produtos favoritos dos clientes.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "API Wishlist funcionando!"}
