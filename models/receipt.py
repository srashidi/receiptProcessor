from decimal import Decimal
from pydantic import BaseModel, StringConstraints, Field, conlist
from typing_extensions import Annotated
import datetime

from models.item import Item


class Receipt(BaseModel):
    retailer: Annotated[str, StringConstraints(pattern="^[\\w\\s\\-&]+$")]
    purchaseDate: datetime.date
    purchaseTime: datetime.time
    items: conlist(Item, min_length=1)
    total: Annotated[Decimal, Field(decimal_places=2, allow_inf_nan=False)]
