import math
from random import randint
import sys
from xml.dom.pulldom import parseString
import numpy as np
from save_dataset import xysave, rasb, saveall


EMPTY_CHAR = 0
AI_TURN = True
USER_TURN = False
user_char = 2
computer_char = 3
scores = {
    user_char: -100,
    computer_char: 100,
    'draw': 0
}
pole = np.zeros((3,3))

list=""
xy=""

def is_win(c, a):
    for i in range(3):
        if a[i][0]==a[i][1]==a[i][2]==c or a[0][i]==a[1][i]==a[2][i]==c or a[0][0]==a[1][1]==a[2][2]==c or a[-1][0]==a[-2][1]==a[-3][2]==c:
            return c

def is_draw(pole):
    count = 0
    for y in range(3):
        count += 1 if EMPTY_CHAR in pole[y] else 0
    return count == 0

def minimax(board, depth, is_ai_turn):
    if is_win(computer_char, board):
        return scores[computer_char]
    if is_win(user_char, board):
        return scores[user_char]
    if is_draw(board):
        return scores['draw']

    if is_ai_turn:
        # выбираем ход который нам выгодней
        best_score = - sys.maxsize
        for y in range(3):
            for x in range(3):
                if board[y][x] == EMPTY_CHAR:
                    board[y][x] = computer_char
                    score = minimax(board, depth + 1, USER_TURN)
                    board[y][x] = EMPTY_CHAR
                    best_score = max(best_score, score)
    else:
        # противник выбирает ход который нам не выгоден
        best_score = sys.maxsize
        for y in range(3):
            for x in range(3):
                if board[y][x] == EMPTY_CHAR:
                    board[y][x] = user_char
                    score = minimax(board, depth + 1, AI_TURN)
                    board[y][x] = EMPTY_CHAR
                    best_score = min(best_score, score)
    return best_score


def xod_pc(pole):
    move = None
    best_score = -sys.maxsize
    board = [pole[y].copy() for y in range(3)]
    for y in range(3):
        for x in range(3):
            if board[y][x] == EMPTY_CHAR:
                board[y][x] = computer_char
                score = minimax(board, 0, USER_TURN)
                board[y][x] = EMPTY_CHAR
                if score > best_score:
                    best_score = score
                    move = (x, y)
    return move

def xod(m,znak):
	x=math.ceil(m/3)-1
	y=m-3*x-1
	global pole
	if pole[x][y]==0:
		pole[x][y]=znak
		return 0
	else:
		print('Эта клетка уже занята!')
		return 1
def get_pc(pole):
    move = None
    best_score = -sys.maxsize
    board = np.copy(pole)
    for y in range(3):
        for x in range(3):
            if board[y][x] == EMPTY_CHAR:
                board[y][x] = computer_char
                score = minimax(board, 0, USER_TURN)
                board[y][x] = EMPTY_CHAR
                if score > best_score:
                    best_score = score
                    move = (x, y)

    return move
def show(pole):
    for i in range(3):
        for j in range(3):
            if pole[i][j]==0:
                print('\033[1;37m'+str(3*i+j+1),end=' ')    
            elif pole[i][j]==2:
                print('\033[36mO',end=' ')
            if pole[i][j]==3:
                print('\033[35mx',end=' ')
        print()

def get_user():
    ll=1
    while ll:
        try:
            m=int(input("Ваш ход: "))
            ll = xod(m,user_char)
        except:
            pass

def xodit():
    pass
while 1:
    kxto=randint(0,1)+2
    pole = np.zeros((3,3))
    while 1:
        

        if kxto==user_char:
            show(pole)
            if is_draw(pole):
                print('is draw')
                break

        
            if is_win(user_char, pole):
                print('you win')
                break
            get_user()
            kxto=computer_char

        
        elif kxto==computer_char:
            move = get_pc(pole)
            if move is not None:
                x, y = move
                list=rasb(pole,list)
                xy=xysave(y,x,xy)
                pole[y][x] = computer_char
                if is_win(computer_char, pole):
                    print('you lose')
                    break
            kxto=user_char
    if input() == "save":
        saveall(list,xy)