# hrací pole
hraci_pole = {
    1:'1', 2:'2', 3:'3', 4:'4', 5:'5',
    6:'6', 7:'7', 8:'8', 9:'9'}
def pozdraveni():
    oddeleni = '=' * 27
    print()
    print('! VÍTEJTE U HRY PIŠKVORKY !')
    print(oddeleni)
    print("""PRAVIDLA HRY:
Každý hráč může umístit 
jednu značku (nebo kámen)
za otáčku na mřížce 3x3. 
Vítězem se stává ten
komu se podaří umístit 
tři své značky v:
* horizontální,
* vertikální popř
* diagonální řadě"""
)
    print(oddeleni)

def show_pole(hraci_pole):
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

def poradi_tahu(tah):
    if tah % 2 == 0:
        return 'O'
    else:
        return 'X' 
""" 
Welcome to Tic Tac Toe
============================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
============================================
Let's start the game
--------------------------------------------
+---+---+---+
| | | |
+---+---+---+
| | | |
+---+---+---+
| | | |
+---+---+---+
============================================
Player o | Please enter your move number: 5
============================================
+---+---+---+
| | | |
+---+---+---+
| | O | |
+---+---+---+
| | | |
+---+---+---+
============================================
Player x | Please enter your move number: 1
============================================
+---+---+---+
| X | | |
+---+---+---+
| | O | |
+---+---+---+
| | | |
+---+---+---+
============================================
Player x | Please enter your move number:
...
============================================
Player o | Please enter your move number:
============================================
+---+---+---+
| X | | |
+---+---+---+
| | O | |
+---+---+---+
| | | |
+---+---+---+
============================================
Congratulations, the player o WON!
============================================
""" 