import numpy as np
import math
board=np.zeros((3,3))

list=''
xy=""
def rasb(pole, list):
	list+='['
	for i in range(3):
		list+='['
		for k in range(3):
			list+=str(int(pole[i][k]))
			if k != 2:
				list+=','
		list+=']'
		if i != 2:
			list+=','
	list+='],'
	
	return list
def xysave(y,x,xy):
	xy+="["+str(y)+", "+str(x)+"],"
	return xy

for i in range(1):
	for i in range(3):
		for j in range(3):
			board[i][j]=2
			list=rasb(board,list)+"\n"
			xy=xysave(i,j,xy)

def saveall(list,xy):
	file=open('ststistic.txt', 'w+')
	file.write(list)
	file.close()

	file=open('ststistic_xy.txt', 'w+')
	file.write(xy)
