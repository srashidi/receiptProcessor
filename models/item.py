from decimal import Decimal
from pydantic import BaseModel, StringConstraints, Field
from typing_extensions import Annotated


class Item(BaseModel):
    shortDescription: Annotated[str, StringConstraints(pattern="^[\\w\\s\\-]+$")]
    price: Annotated[Decimal, Field(decimal_places=2, allow_inf_nan=False)]
