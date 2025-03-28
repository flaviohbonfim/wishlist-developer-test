from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="API de Produtos",
    description="Mock de API para listar produtos fictícios.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
