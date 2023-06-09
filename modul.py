# hrací pole
hraci_pole = {
    1:'1', 2:'2', 3:'3', 4:'4', 5:'5',
    6:'6', 7:'7', 8:'8', 9:'9'}
oddeleni = '=' * 29
# úvod hry
def pozdraveni():
    
    print()
    print('!  VÍTEJTE U HRY PIŠKVORKY  !')
    print(oddeleni)
    print("""PRAVIDLA HRY:
Každý hráč může umístit 
jednu značku (nebo kámen)
za tah na mřížce 3x3. 
Vítězem se stává ten
komu se podaří umístit 
tři své značky v:
* horizontální,
* vertikální popř
* diagonální řadě"""
)
    print(oddeleni)
# Zobrazení hrací plochy
def zobrazeni_pole(hraci_pole):
    oddelovac = ('+---+---+---+')
    
    print(f"""
       {oddelovac}
       | {hraci_pole[1]} | {hraci_pole[2]} | {hraci_pole[3]} |
       {oddelovac}
       | {hraci_pole[4]} | {hraci_pole[5]} | {hraci_pole[6]} |
       {oddelovac}
       | {hraci_pole[7]} | {hraci_pole[8]} | {hraci_pole[9]} |
       {oddelovac}
    """,)
# funce na pořadí tahu hráčů
def poradi_tahu(tah):
    if tah % 2 == 0:
        return 'O'
    else:
        return 'X' 
# Program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen tříkrát. Pokud ano, vyhrává hráč, kterému tyto tři kameny patří
def podminka_vitezstvi(hraci_pole):
    #horizontální
    if (hraci_pole[1] == hraci_pole[2] == hraci_pole[3]) \
        or (hraci_pole[4] == hraci_pole[5] == hraci_pole[6]) \
        or (hraci_pole[7] == hraci_pole[8] == hraci_pole[9]):
        return True
    # vertikální
    elif (hraci_pole[1] == hraci_pole[4] == hraci_pole[7]) \
        or (hraci_pole[2] == hraci_pole[5] == hraci_pole[8]) \
        or (hraci_pole[3] == hraci_pole[6] == hraci_pole[9]):
        return True
    # diagonálně
    elif (hraci_pole[1] == hraci_pole[5] == hraci_pole[9]) \
        or (hraci_pole[3] == hraci_pole[5] == hraci_pole[7]):
        return True
    else:
        return False
