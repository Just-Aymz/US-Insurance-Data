from pydantic import BaseModel
from enum import Enum
from typing import Optional

# Enum for categorical features
class SmokerStatus(Enum):
    yes = "yes"
    no = "no"

class Sex(Enum):
    male = "male"
    female = "female"

class Region(Enum):
    south_west = "southwest"
    south_east = "southeast"
    north_west = "northwest"
    north_east = "northeast"

class InputFeatures(BaseModel):
    age: float
    bmi: float
    children: int
    sex: Sex
    smoker: SmokerStatus
    region: Region

    """
    The Config class with use_enum_values = True ensures that Pydantic 
    uses the actual values of the Enum fields when serializing the data,
    making the API response and request handling more user-friendly.
    """
    class Config:
        use_enum_values = True
