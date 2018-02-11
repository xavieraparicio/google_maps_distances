#import urllib.request
import json
import pandas as pd
import numpy as np
from operator import itemgetter

import api_key_file

class Distance_Calculator:
    def hello_world_method(self):
        print("hello world")

    def reading_postcodes_for_origin_point(self,csv_file_with_postcodes_for_origin_point):
        postcodes_for_origin_point = pd.read_csv(csv_file_with_postcodes_for_origin_point)
        return(postcodes_for_origin_point)

    def printing_read_postcodes(self,csv_file_with_postcodes_for_origin_point):
        postcodes_for_origin_point = self.reading_postcodes_for_origin_point(csv_file_with_postcodes_for_origin_point)
        for postcode in postcodes_for_origin_point.Postcodes:
            print(postcode)
        return
