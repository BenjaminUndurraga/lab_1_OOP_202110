from numpy import random
import numpy as np

cards_to_play = int(input('with how many pairs of cards you want to play?: '))
cards = []
player1=0
player2=0
turn = 0
total_points=0

#crearemos los pares de cartas a jugar
card_creator = 1
while card_creator <= cards_to_play:
    cards.append(card_creator)
    cards.append(card_creator)
    card_creator+=1
'''
print(cards), estan bien creadas, falta desordenarlas, para esto tendremos 
que ponerlas en otra lista
'''
messy_cards = []

while len(cards)>0:
    messing_up = cards[random.randint(len(cards))]
    messy_cards.append(messing_up)
    cards.remove(messing_up)
'''
sacamos las cartas de cards y las pusimos en messy_cards desordenadas.
ahora tenemos que pasar messy_cards a matriz para que sea un tablero con coordenadas.
'''

board = np.array(messy_cards).reshape(2,cards_to_play)
#lo hacemos de dos columnas debido a que 2 es el minimo de cartas totales a jugar
print(board)

# tenemos el tablero pero falta definir el que lo ocultara

def silenced_board(rows,amount):
    m=[]
    for i in range(rows):
        rows=[]
        for j in range(amount):
            rows.append(' *')
        m.append(rows)
    return m

move = silenced_board(2,cards_to_play)
print(move)
print(board[0][1])

def play(x,y):
    coordx = int(input(('give me your x coordinate')
    coordy = int(input('give me your y coordinate'))
    l=[]
    for i in board:
        l.append

