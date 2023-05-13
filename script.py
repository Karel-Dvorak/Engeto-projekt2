"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Karel Dvořák
email: dvorak.karl@seznam.cz
discord: Karel_D#8322
"""
from modul import show_pole, hraci_pole, pozdraveni
from modul import poradi_tahu

#Program pozdraví uživatele
#Vypíše v krátkosti pravidla hry
pozdraveni()

hra_bezi = True
tah = 0

#Zobrazí hrací plochu
while hra_bezi:
    show_pole(hraci_pole)
    print(f'Hráč {poradi_tahu(tah + 1)} zadej číslo pole nebo "q" pro ukončení')
    #Vyzve prvního hráče, aby zvolil pozici pro umístění hracího kamene
    vyber = input('Výběr: ')
    if vyber == 'q':
        hra_bezi = False

    #Jakmile hráč úspěšně vybere pole, zobrazíme nový stav hrací plochy
    elif str.isdigit(vyber) and int(vyber) in hraci_pole:
        if not hraci_pole[int(vyber)] in {'X','O'}:
            tah += 1
            hraci_pole[int(vyber)] = poradi_tahu(tah)

        #Pokud se na vybraném poli nachází hrací kámen druhého hráče, program jej upozorní, že je pole obsazené
        else:
            print('Pole je obsazené! Vyber jiné!')

    #Pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní.
    elif not str.isdigit(vyber):
        print('Nezadal jsi číslo!!')

    #Pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní.
    elif int(vyber) > 9 or int(vyber) <= 0:
        print('Zadal jsi číslo mimo hrací pole!')



#Program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen tříkrát. Pokud ano, vyhrává hráč, kterému tyto tři kameny patří
#Pokud nezbývá žádné volné hrací pole a žádný hráč nevyhrál, jde o remízu.