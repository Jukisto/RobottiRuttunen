'''
Created on 11.2.2021

@author: Jere Eskelinen
'''


import datetime
import json
from urllib.request import Request, urlopen


viikonpaivat = ("- Maanantai", "- Tiistai", "- Keskiviikko", "- Torstai", "- Perjantai")

paivays = datetime.date.today()
vuosi, viikko, paiva = paivays.isocalendar()

def resetLiha():
    ruokalista = open("ruokalistaLiha.txt", "w")
    ruokalista.truncate(0)
    ruokalista.write("```diff\n")
    ruokalista.close()
    
def resetKasvis():
    ruokalista = open("ruokalistaKasvis.txt", "w")
    ruokalista.truncate(0)
    ruokalista.write("```diff\n")
    ruokalista.close()
    
def kirjoitaLiha(ruuat):
    with open('ruokalistaLiha.txt', 'a') as outfile:
        outfile.write(ruuat)
        outfile.write("\n")
        outfile.close()        
          
def kirjoitaKasvis(ruuat):
    with open('ruokalistaKasvis.txt', 'a') as outfile:
        outfile.write(ruuat)
        outfile.write("\n")
        outfile.close() 
        
def liha():
    kirjoitaLiha("- Viikko : " + str(viikko) + "\n")
    i = 0
    for mealdates in obj['mealdates']:
        lista = mealdates['courses']
        kirjoitaLiha(viikonpaivat[i])
        i += 1
        kirjoitaLiha("+ " + lista['1']['title_fi'] + " \n ")         

def kasvis():
    kirjoitaKasvis("- Viikko : " + str(viikko) + "\n")
    i = 0
    for mealdates in obj['mealdates']:
        lista = mealdates['courses']
        kirjoitaKasvis(viikonpaivat[i])
        i += 1
        kirjoitaKasvis("+ " + lista['2']['title_fi']  + " \n ")

def finishLiha():
    with open('ruokalistaLiha.txt', 'a') as outfile:
        outfile.write("```")
        outfile.close()
        
def finishKasvis():
    with open('ruokalistaKasvis.txt', 'a') as outfile:
        outfile.write("```")
        outfile.close()
        
req = Request('https://www.sodexo.fi/ruokalistat/output/weekly_json/10229', headers={'User-Agent': 'Mozilla/6.9'})
webpage = urlopen(req).read()

obj = json.loads(webpage)
    