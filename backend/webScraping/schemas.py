from ninja import Schema
from typing import Optional
from decimal import Decimal


# -------- TbImoveis --------
class TbImoveisSchema(Schema):
    id: int
    titulo: Optional[str] = None
    preco: Optional[Decimal] = None
    metragem: Optional[Decimal] = None
    quarto: Optional[int] = None
    descricao: Optional[str] = None


class TbImoveisSchemaIn(Schema):
    titulo: Optional[str] = None
    preco: Optional[Decimal] = None
    metragem: Optional[Decimal] = None
    quarto: Optional[int] = None
    descricao: Optional[str] = None
