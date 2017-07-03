# -*- coding: utf-8 -*-

dodole = "Oj, dodole, mili Bože\noj, dodo, dodole\nNaša doda Boga moli\noj, dodo, dodole\nSitna kiša da zarosi\noj, dodo, dodole\nNaša polja da potopi\noj, dodo, dodole\nI da rodi bel' pšenica\noj, dodo, dodole\nI kukuruz sa dva klasa\noj, dodo, dodole\nŠto molila umolila\noj, dodo, dodole\nSitna kiša zarosila\noj, dodo, dodole\nNaša polja potopila\noj, dodo, dodole\nI rodila bel' pšenica\noj, dodo, dodole\nI kukuruz sa dva klasa\noj, dodo, dodole"
lista_stihova = dodole.split("\n")


for i in range (len(lista_stihova)-1,0,-1):
    print(lista_stihova[i])
    
    lista_reči = lista_stihova.split(" ")
    for x in range (len(lista_reči)-1, 0, -1):
        print(lista_reči[x])
    
    
    
