"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Karel Dvořák
email: dvorak.karl@seznam.cz
discord: Karel_D#8322
"""
from modul import zobrazeni_pole, hraci_pole, pozdraveni
from modul import poradi_tahu, podminka_vitezstvi, oddeleni

#Program pozdraví uživatele
#Vypíše v krátkosti pravidla hry
pozdraveni()

hra_bezi = True
tah = 0

#Zobrazí hrací plochu
while hra_bezi:
    zobrazeni_pole(hraci_pole)
    print(oddeleni)
    print(f'Hráč {poradi_tahu(tah + 1)} zadej číslo pole')
    print('q = quit'.rjust(29))

    #Vyzve prvního hráče, aby zvolil pozici pro umístění hracího kamene
    vyber = input('Výběr: ')
    print(oddeleni)
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
        print('Nezadal jsi číslo!')
        print('-' * 29)

    #Pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní.
    elif int(vyber) > 9 or int(vyber) <= 0:
        print('Číslo je mimo hrací pole!')
        print('-' * 29)

    #Program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen tříkrát. Pokud ano, vyhrává hráč, kterému tyto tři kameny patří
    if podminka_vitezstvi(hraci_pole):
        hra_bezi = False
        zobrazeni_pole(hraci_pole)
        print(oddeleni)
        print(f'!!! VYHRÁL HRÁČ {poradi_tahu(tah)} !!!'.center(29))

    #Pokud nezbývá žádné volné hrací pole a žádný hráč nevyhrál, jde o remízu.
    if tah > 8 and not podminka_vitezstvi(hraci_pole): 
        hra_bezi = False
        zobrazeni_pole(hraci_pole)
        print(oddeleni)
        print('!!! NIKDO NEVYHRÁL !!!'.center(29))
    
print('KONEC HRY'.center(29))
