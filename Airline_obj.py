from datetime import date
from typing import Optional
from pydantic import BaseModel, StrictStr

class Preferences(BaseModel):
    start: date
    end: date
    origin: StrictStr
    destination: StrictStr
    travelers: int


test_dict = {
    'start' : '2023-06-21',
    'end' : '2023-06-27',
    'origin' : 'Seattle',
    'destination' : 'New York',
    'travelers' : 2
}

traveler = Preferences.parse_obj(test_dict)

print(traveler.dict())