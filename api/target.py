import json
import requests
from datetime import datetime

# Change api_key to redcircle api key
api_key = None

def get_params(id):
    '''
    Get parameters for redcircle api
    '''
    res = {"api_key": api_key, "type": "product", "dpci": id}
    return res

def check_cache(cache, id):
    '''
    Check if id in cache
    '''
    for i in cache:
        if i['id'] == id:
            return i
    return

def check_meat(s):
    '''
    Given list of breadcrumbs, return if is meat
    '''

    meat = False

    for i in s:
        if meat:
            return True, i['name']

        if 'meat' in i['name'].lower():
            meat = True
    return meat, ''
  
def get_info(lis_ids, cache_filename = 'cache.json'):
    res = []
    """ 
    Make a dictionary for each id.

    {
    "Success" : ,
    "Id" : ,
    "Price": ,
    "Is meat": ,
    "Type of meat": ,
    "Is processed": ,
    "Nutrients': 
    "Weight" : ,
    "Date accessed" : 
    }
    """
    with open(cache_filename, 'r') as f:
        cache = json.load(f)

    res = []

    for id in lis_ids:
        print('Checking id', id)
        info_dict = check_cache(cache, id)

        if info_dict:
            if info_dict['success']:
                res.append(info_dict)
        else:
            info_dict = {}

            api_result = requests.get(
                "https://api.redcircleapi.com/request", get_params(id)
            )
            info = api_result.json()

            if info['request_info']['success']:
                info_dict['success'] = True

                info_dict["id"] = id

                info_dict["price"] = info['product']["buybox_winner"]["price"]["value"]
                
                if 'nutrients' in info['product']:
                    info_dict['nutrients'] = info['product']['nutrients']

                is_meat, name = check_meat(info['product']['breadcrumbs']) 
                info_dict['is meat'] = is_meat
                info_dict['type of meat'] = name

                info_dict['is processed'] = 'price per lb' in info['product']['title']

                info_dict['weight'] = info['product']['weight']

                info_dict['date accessed'] = str(datetime.now())

                cache.append(info_dict)
                
                res.append(info_dict)
            else:
                info_dict['success'] = False
                info_dict["id"] = id
                cache.append(info_dict)

    with open(cache_filename, 'w') as f:
        json.dump(cache, f)

    return res
