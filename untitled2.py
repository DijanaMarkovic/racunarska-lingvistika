# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 17:23:29 2017

@author: Korsnik
"""

telefonski_imenik = {"Paja Patak": 123456, "Mini Maus": 234567, "Šilja": 345678}
vukajlija = {"sojanica": "Posna pljeskavica. Garantovano bez trihinele.", "jahanje": "Omiljena aktivnost šefova za koju je potrebno da radnik ima konjske živce.", "šef": "Čovek koji nema smisao za umor."}
vrste_reči = {"imenice": ["polaznik", "seminar", "lingvistika", "Isidora"], "glagoli": ["slušati", "crtati", "jesti"], "zamenice": ["on", "ona", "ono"]}

print(telefonski_imenik["Mini Maus"])
print(vrste_reči["imenice"])
print(vukajlija["šef"])

vukajlija["šef"] = "Miloš"
print(vukajlija)

print(telefonski_imenik.keys())
print(telefonski_imenik.values())

print(vrste_reči["imenice"][2])

del telefonski_imenik["Mini Maus"]
print(telefonski_imenik)