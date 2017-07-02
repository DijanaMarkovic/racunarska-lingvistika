# -*- coding: utf-8 -*-
rečnik = {"lep":{"sinonimi":["naočit", "krasan"], "antonimi":["ružan","rugoban"]}, "buka":{"sinonimi":["galama", "vika"], "antonimi":["tišina", "bezglasje"]}, "vredan":{ "sinonimi":["radan", "marljiv"], "antonimi":["lenj", "neradan"]}} 
#{}
#[]
print(rečnik["lep"]["sinonimi"]) 
print(rečnik["lep"]["antonimi"])
print(rečnik["buka"]["sinonimi"]) 
print(rečnik["buka"]["antonimi"])
print(rečnik["vredan"]["sinonimi"]) 
print(rečnik["vredan"]["antonimi"])

print(rečnik["lep"]["sinonimi"][0]) 
print(rečnik["lep"]["antonimi"][1])
print(rečnik["buka"]["sinonimi"][0]) 
print(rečnik["buka"]["antonimi"][1])
print(rečnik["vredan"]["sinonimi"][0]) 
print(rečnik["vredan"]["antonimi"][1])

rečnik=#TODO

for reč in rečnik.keys():
    
    print("Reč: ", reč) 
    sin = "Sinonimi: "
    ant = "Antonimi: "

    for sinonim in rečnik[reč]["sinonimi"]:
        sin += sinonim + ", "
    print(sin[:-2])

    for antonim in rečnik[reč]["antonimi"]:
        ant += antonim + ", "    
    print(ant[:-2] + "\n")