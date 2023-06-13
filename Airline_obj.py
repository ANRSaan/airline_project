from datetime import date
from typing import Optional
from pydantic import BaseModel, StrictStr
import json

with open("preferences") as f:
    data = json.load(f)


class Preferences(BaseModel):
    start: date
    end: date
    origin: StrictStr
    destination: StrictStr
    travelers: int

traveler = Preferences.parse_obj(data)

print(traveler.dict())