#import urllib.request
import json
import pandas as pd
import numpy as np
from operator import itemgetter

#import api_key_file

class Distance_Calculator:
    def hello_world_method(self):
        print("hello world")

    def read_postcodes(self,postcodes_csv):
        df_postcodes = pd.read_csv(postcodes_csv)
        return(df_postcodes)

    def print_postcodes(self,df_Postcodes):
        #df_Postcodes = self.read_postcodes(postcodes_csv)
        for postcode in df_Postcodes.Postcodes:
            print(postcode)
        return

    def create_string_for_request(self,df_Postcodes):
        string = ''
        for index, postcode in enumerate(df_Postcodes.Postcodes):
            string += postcode.replace(" ","+")
            if (index+1) != df_Postcodes.shape[0]:
                string += "|"
        return(string)
