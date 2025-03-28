from pydantic import BaseModel
from typing import Optional

class Produto(BaseModel):
    id: int
    title: str
    price: float
    image: str
    brand: str
    reviewScore: Optional[float]
