from pydantic import BaseModel,Field, StringConstraints
from typing_extensions import Annotated


class Zipcode(BaseModel):
    zipcode: int
    page: int

class Counties(BaseModel):
    state :  Annotated[str,StringConstraints(to_lower=True)]
    page:int = Field(...,ge=1)

class TwoLocation(BaseModel):
    latitude1 : float = Field(..., ge = -90, le= 90)
    longitude1 : float = Field(..., ge=-180, le=180)
    latitude2 : float = Field(..., ge = -90, le= 90)
    longitude2 : float = Field(..., ge=-180, le=180)

class TwoZipcode(BaseModel):
    zipcode1: int 
    zipcode2 : int 

class Location(BaseModel):
    latitude : float = Field(..., ge = -90, le= 90) 
    longitude : float = Field(..., ge=-180, le=180)



