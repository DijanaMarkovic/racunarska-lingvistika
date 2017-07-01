# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 17:23:54 2017

@author: Korsnik
"""

niska = "Milena je sinoć videla Mitra, nežnog, zelenog skakavca ispred stacionara i uzviknula je: \"Ju, Mitre, uplašio si me!\". Ali Mitar se na to nije obazirao - žustro je skočio u Mileninom pravcu. Videvši to, Milena polete preko dvorišta i polete ka stacionaru brzinom svetlosti. Nažalost, svetlost je brža od automatskog mehanizma za otvaranje vrata. I tako ostade Milenin trag na ulaznim vratima IS Petnica."
niska= niska.lower()
reci=niska.split(" ")
#print(reci)
reci[4] = reci[4][:-1]
reci[5] = reci[5][:-1]
reci[13] = reci[13][1:-1]
reci[14]= reci[14][:-1]
reci[12]= reci[12][:-1]
reci[17]= reci[17][:-3]
reci[31]= reci[31][:-1]
reci[33] = reci[33][:-1]
reci[43] = reci[43][:-1]
reci[44] = reci[44][:-1]
reci[53] = reci[53][:-1]
reci[63] = reci[63][:-1]

print(reci)