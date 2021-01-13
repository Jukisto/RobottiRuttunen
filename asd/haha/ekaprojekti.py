'''
Created on 11.1.2021

@author: jallu
'''

if __name__ == '__main__':
    pass

import json
import pprint
from urllib.request import Request, urlopen


def reset():
    ruokalista = open("ruokalistaMuokattu.txt", "w")
    ruokalista.truncate(0)
    ruokalista.close()

# Writes all the names of the foods.
def kirjoita(ruuat):
    with open('ruokalistaMuokattu.txt', 'a') as outfile:
        pprint.pprint(ruuat, outfile)
        outfile.close()
        
# Checks if the letter is uppercase and joins them into words.       
def isot_kirjaimet(nimet):
    return "".join(kirjain for kirjain in nimet if kirjain.isupper())


# Writes the text that is uppercase after 'name' tag + 1 line.  Uses kirjoita function.   
def paivanRuoka(paiva):
    with open('ruokalista.txt', 'r') as f:
        searchlines = f.readlines()
        kirjoita(paiva)
        for i, line in enumerate(searchlines):
            if "'name'" in line:
                for l in searchlines[i:i+1]:
                    kirjoita(isot_kirjaimet(l))
                    f.close()
                    
                    
                    
# Resets the muokattuRuokalista.txt file to empty text file.    
reset()   
    
# download raw json object
req = Request('https://www.sodexo.fi/ruokalistat/output/weekly_json/10229', headers={'User-Agent': 'Mozilla/6.9'})
webpage = urlopen(req).read()

# parse json object
obj = json.loads(webpage)


# Create ruokalista.txt if it does not exists. Cleans JSON to more readable format.
with open('ruokalista.txt', 'w') as outfile:
    pprint.pprint(obj, outfile)
    outfile.close()

# Writes all the meals of the week, needs fixing. Writes the chosen text infront of the text file.    
paivanRuoka("Maanantai")
