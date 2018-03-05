import requests
import json
from   api_key_file import api_key
import pandas as pd
import numpy  as np
#from operator import itemgetter

#import api_key_file

class Distance_Calculator:

    def hello_world_method(self):
        return("hello world")

    def read_postcodes(self,postcodes_csv):
        df_postcodes = pd.read_csv(postcodes_csv)
        return(df_postcodes)

    def print_postcodes(self,df_Postcodes):
        #df_Postcodes = self.read_postcodes(postcodes_csv)
        for postcode in df_Postcodes.Postcodes:
            print(postcode)
        return

    def transform_postcode_into_google_readable(self,df_Postcodes):
        string = ''
        for index, postcode in enumerate(df_Postcodes.Postcodes):
            string += postcode.replace(" ","+")
            if (index+1) != df_Postcodes.shape[0]:
                string += "|"
        return(string)

    special_postcodes = { 'GU13' : 'GU13+CHURCH+CROCKAM',
                          "S4"   : 'S4+SHEFFIELD',
                          "S6"   : 'S6+SHEFFIELD',
                          "PA34" : 'OBAN+PA34',
                          "PH41" : 'MALLAIG+PH41'}

### Add a method that stores origins and destinations

    def create_full_string_for_request(self,
                                       origin_addresses,
                                       destination_addresses,
                                       api_key):

        endpoint    = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        nav_request = 'origins={}&destinations={}&key={}'.format(origin_addresses,
                                                                 destination_addresses,
                                                                 api_key)
        request = endpoint + nav_request
        return(request)

    def concatenate_read_method(self, addresses_file):
        addresses = self.read_postcodes(addresses_file)
        addresses = self.transform_postcode_into_google_readable(addresses)
        return(addresses)

    def concatenate_method(self,
                           origins_file,
                           destinations_file,
                           api_key):

        origin_addresses      = self.concatenate_read_method(origins_file)
        destination_addresses = self.concatenate_read_method(destinations_file)
        navigation_request    = self.create_full_string_for_request(origin_addresses,
                                                                    destination_addresses,
                                                                    api_key)
        return(navigation_request)

    def call_google_maps(self, navigation_request):
        response   = requests.get(navigation_request)
        directions = response.json()
        return(directions)

    def extract_variables_from_response(self,
                                       json_response,
                                       variable_to_extract,
                                       origin_addresses):
        
        dictionary  = {}
        origin_list = origin_addresses['Postcodes'].tolist() ## Need to make that more general
        for index, response in enumerate(json_response):
            try:
                origin             = origin_list[index]
                variable_list     = []
                for route in response['elements']:
                    variable_list.append(route[variable_to_extract]['value'])
                    dictionary[origin] = variable_list
            except Exception:
                pass
        return (dictionary)


    def create_dataframe_from_response(self, 
                                       directions, 
                                       variable_to_extract,
                                       origin_addresses,
                                       destination_addresses):

        json_response = directions['rows']
        dictionary    = self.extract_variables_from_response(json_response,
                                                             variable_to_extract,
                                                             origin_addresses)
        dataframe     = pd.DataFrame(dictionary, index = destination_addresses['Postcodes'].tolist())        

        return (dataframe)






#    def concatenate_methods():
#        a = transform_postcode_into_google_readable(whatever)
#        create_full_string_for_request(a,b)
