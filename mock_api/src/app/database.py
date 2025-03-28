import json
import os
from app.models import Produto

ARQUIVO_JSON = "produtos.json"

def salvar_produtos(produtos):
    """ Salva os produtos no arquivo JSON. """
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump([produto.dict() for produto in produtos], f, indent=4)

def carregar_produtos():
    """ Carrega os produtos do arquivo JSON, se existir. """
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            return [Produto(**item) for item in json.load(f)]
    return None
