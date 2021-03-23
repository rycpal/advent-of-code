# Day 22: Crab Combat
# <ryc> 2021

import re

def inputdata():
    with open('day_22_2020.input') as stream:
        data = stream.readlines()
        data.pop(0)
        player1 = list()
        item = data.pop(0)
        while len(item) != 1:
            player1.append(int(item))
            item = data.pop(0)
        data.pop(0)
        player2 = list()
        while len(data) != 0:
            player2.append(int(data.pop(0)))
    return player1, player2

def playing_normal(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        if player1[0] > player2[0]:
            player1.append(player1.pop(0))
            player1.append(player2.pop(0))
        else:
            player2.append(player2.pop(0))
            player2.append(player1.pop(0))
    winner = player1 if len(player2) == 0 else player2
    score = 0
    for index in range(len(winner)):
        score += winner[index] * (len(winner) - index)
    return score

def playing_recursive(player1, player2):
    stack = list()
    decks = list()
    while len(stack) > 0 or (len(player1) > 0 and len(player2) > 0):
        if [player1,player2] in decks:
            player2 = list()
        decks.append([player1.copy(), player2.copy()])
        if len(player1) == 0:
            player1, player2, decks = stack.pop()
            player2.append(player2.pop(0))
            player2.append(player1.pop(0))
        elif len(player2) == 0:
            player1, player2, decks = stack.pop()
            player1.append(player1.pop(0))
            player1.append(player2.pop(0))
        elif player1[0] < len(player1) and player2[0] < len(player2):
            stack.append([player1.copy(), player2.copy(), decks])
            player1 = player1[1:(player1[0]+1)]
            player2 = player2[1:(player2[0]+1)]
            decks = list()
        elif player1[0] > player2[0]:
            player1.append(player1.pop(0))
            player1.append(player2.pop(0))
        else:
            player2.append(player2.pop(0))
            player2.append(player1.pop(0))
    winner = player1 if len(player2) == 0 else player2
    score = 0
    for index in range(len(winner)):
        score += winner[index] * (len(winner) - index)
    return score

if __name__ == '__main__':
    print('\n22: Crab Combat')
    player1, player2 = inputdata()
    print('\nscore normal =', playing_normal(player1.copy(), player2.copy()))
    print('\nscore recursive =', playing_recursive(player1, player2))
