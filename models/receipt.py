from decimal import Decimal
from pydantic import BaseModel
import datetime

from models.item import Item


class Receipt(BaseModel):
    retailer: str
    purchaseDate: datetime.date
    purchaseTime: datetime.time
    items: list[Item]
    total: Decimal
