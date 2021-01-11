'''
Created on 11.1.2021

@author: jallu
'''

if __name__ == '__main__':
    pass

import json
import pprint
from urllib.request import Request, urlopen

# download raw json object
req = Request('https://www.sodexo.fi/ruokalistat/output/weekly_json/10229', headers={'User-Agent': 'Mozilla/6.9'})
webpage = urlopen(req).read()

# parse json object
obj = json.loads(webpage)

# output all attributes from the site
# print(obj)


#Create ruokalista.txt if it does not exists. Cleans JSON to more readable format.
with open('ruokalista.txt', 'w') as outfile:
    pprint.pprint(obj, outfile)

# pprint.pprint(obj)