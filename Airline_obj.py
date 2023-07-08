from datetime import date
from typing import Optional
from pydantic import BaseModel, StrictStr
import json


class Preferences(BaseModel):
    start: date
    end: date
    origin: StrictStr
    destination: StrictStr
    travelers: int
    airlines: StrictStr
