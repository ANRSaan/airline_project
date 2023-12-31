from datetime import date
from typing import Optional
from pydantic import BaseModel, StrictStr
import pandas

class Searcher:
    def __init__(self, airlines: list) -> None:
        self.airlines = airlines
        pass

    def airline_search(self, Preferences):
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
    
    def results(self, results, Preferences):
        '''
            This is where the Selenium results object gets put into a csv file,
            based around the original Preferences object.
        '''