from datetime import date
from typing import Optional
from pydantic import BaseModel, StrictStr
import json
from Airline_obj import Preferences, traveler
from Airline_return import AirlineList

AIRLINES = ['southwest', 'alaska']

def main():
    with open("preferences") as f:
        data = json.load(f)


    traveler = Preferences.parse_obj(data)
    searcher = Searcher(airlines=AIRLINES)
    searcher.search(traveler)

    results = AirlineList.airline_getter(traveler)

    AirlineList.airline_parser(results)