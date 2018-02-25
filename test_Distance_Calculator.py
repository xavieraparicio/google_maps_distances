import pytest

from Distance_Calculator import Distance_Calculator
from api_key_file        import api_key

def test_hello_world_method():
    assert Distance_Calculator().hello_world_method() == 'hello world'

def test_am_I_getting_a_Json_file():
    test               = Distance_Calculator()
    navigation_request = test.concatenate_method(origins_file      = 'origin_postcodes.csv',
                                                 destinations_file = 'destination_postcodes.csv',
                                                 api_key           = api_key())
    destinations       = test.call_google_maps(navigation_request)
    assert type(destinations) ==  dict
