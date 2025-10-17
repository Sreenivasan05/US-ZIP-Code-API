from pydantic import BaseModel,Field, StringConstraints
from typing_extensions import Annotated


class Zipcode(BaseModel):
    zipcode: int
    page: int

class Counties(BaseModel):
    state :  Annotated[str,StringConstraints(to_lower=True)]
    page:int = Field(...,ge=1)
