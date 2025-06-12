from ninja import Schema
from typing import Optional
from decimal import Decimal

# -------- TbImoveis --------
class TbImoveisSchema(Schema):
    id: int
    localizacao: Optional[str] = None
    metragem: Optional[Decimal] = None
    preco: Optional[Decimal] = None
    quartos: Optional[int] = None
    decricao: Optional[str] = None


class TbImoveisSchemaIn(Schema):
    localizacao: Optional[str] = None
    metragem: Optional[Decimal] = None
    preco: Optional[Decimal] = None
    quartos: Optional[int] = None
    decricao: Optional[str] = None