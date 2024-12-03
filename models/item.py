from decimal import Decimal
from pydantic import BaseModel


class Item(BaseModel):
    shortDescription: str
    price: Decimal
