import random
from fastapi import APIRouter, HTTPException, Query
from typing import List
from faker import Faker
from app.models import Produto
from app.database import carregar_produtos, salvar_produtos
from app.services import get_product_image

router = APIRouter()
faker = Faker()

produtos_mock = carregar_produtos()
if produtos_mock is None:
    produtos_mock = []
    categorias = ["electronics", "furniture", "clothing", "shoes", "accessories"]

    for i in range(1, 51):
        categoria = random.choice(categorias)
        produtos_mock.append(Produto(
            id=i,
            title=faker.word().capitalize() + " " + faker.word().capitalize(),
            price=round(random.uniform(10, 5000), 2),
            image=get_product_image(categoria),
            brand=faker.company(),
            reviewScore=round(random.uniform(1, 5), 1) if random.random() > 0.2 else None
        ))

    salvar_produtos(produtos_mock)

@router.get("/api/product/", response_model=List[Produto])
def listar_produtos(page: int = Query(1, alias="page", ge=1)):
    """ Retorna uma lista paginada de produtos. """
    start = (page - 1) * 10
    end = start + 10
    produtos_paginados = produtos_mock[start:end]

    if not produtos_paginados:
        raise HTTPException(status_code=404, detail="Página não encontrada")

    return produtos_paginados

@router.get("/api/product/{product_id}/", response_model=Produto)
def detalhe_produto(product_id: int):
    """ Retorna os detalhes de um produto pelo ID. """
    produto = next((p for p in produtos_mock if p.id == product_id), None)

    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return produto
