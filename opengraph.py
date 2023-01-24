# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API

"""
# leWagon='https://opengraph.lewagon.com/?url=https://www.lewagon.com'

import requests

def fetch_metadata(url):
    """
    Return a dictionary of OpenGraph metadata found in HTML of given url
    """
    base_url = "https://opengraph.lewagon.com"
    try :
        res=requests.get(base_url, params={'url': url}).json()
        return res['data']
    except:
        return {}

# To manually test, please uncomment the following lines and run `python opengraph.py`:
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(fetch_metadata("https://www.github.com"))
