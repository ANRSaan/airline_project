from datetime import date
from typing import Optional
from pydantic import BaseModel, StrictStr
import json
from Airline_obj import traveler

class AirlineList:
    def __init__(self, airlines: list) -> None:
        self.airlines = airlines
        pass

    def airline_getter(self, traveler):
        for airline in self.airlines:
            launch_specific_selenium()
        results = {}
        ''' 
            This is where the bit that sends the Preferences object off to the 
            Selenium scripts goes
        '''

        '''
            This is where the bit that waits for the Selenium scripts
            to finish goes.  It will deposite the returns from those scripts into
            the results object.
            
        '''

        return results
    
    def airline_parser(results):
        """
            This is the bit where we take the results from airline_getter
            and spread them out into something the user can look at.
        """