from datetime import date
from typing import Optional
from pydantic import BaseModel, StrictStr
import json
from Airline_obj import Preferences
from Airline_return import Searcher

AIRLINES = [Preferences.airlines]

def main():
    with open("preferences") as f:
        data = json.load(f)


    traveler = Preferences.parse_obj(data)
    searcher = Searcher(airlines=AIRLINES)
    
    results = searcher.airline_search(traveler)