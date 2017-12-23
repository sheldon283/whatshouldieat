# -*- coding: utf-8 -*-

from __future__ import print_function
from random import *

import json
import pprint
import requests
import sys
import urllib
import os


try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

API_KEY = os.environ.get('YELP_API_KEY')
# API constants
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.

# Default values.
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'

SEARCH_LIMIT = 50

def ask(host, path, api_key, url_params=None):
    # """Given your API_KEY, send a GET request to the API.
    # Args:
    #     host (str): The domain host of the API.
    #     path (str): The path of the API after the domain.
    #     API_KEY (str): Your API Key.
    #     url_params (dict): An optional set of query parameters in the request.
    # Returns:
    #     dict: The JSON response from the request.
    # Raises:
    #     HTTPError: An error occurs from the HTTP request.
    # """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()


def search(keyword, location):
    # """Query the Search API by a search term and location.
    # Args:
    #     term (str): The search term passed to the API.
    #     location (str): The search location passed to the API.
    # Returns:
    #     dict: The JSON response from the request.
    # """
    url_params = {
        'term': keyword,
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return ask(API_HOST, SEARCH_PATH, API_KEY, url_params=url_params)

def query_api(response):
    # """Pick a random business from the request object generated by ask.
    # Args:
    #   response (obj): The request object created by ask
    # Returns: 
    #   business (list): A list that is part of the request object
    # """
    businesses = response.get('businesses')
    length = len(businesses)
    if (length == 0):
        return None
    x = randint(0,length-1)
    return businesses[x]

def getReviews(business):
    businessID = business['id']
    path = BUSINESS_PATH + businessID + '/reviews'
    response = ask(API_HOST, path, API_KEY, None)
    return ask(API_HOST, path, API_KEY, None)
