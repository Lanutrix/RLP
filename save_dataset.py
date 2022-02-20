import numpy as np
import math
import os
board=np.zeros((3,3))
def rasb(pole):
	list=""
	list+='['
	for i in range(3):
		list+=''
		for k in range(3):
			list+=str(int(pole[i][k]))
			if k != 2:
				list+=','
		list+=''
		if i != 2:
			list+=','
	list+='],'
	cd='cd /home/dmodv/git_project/testing/ && '
	os.system(cd+"touch savepole.txt")
	os.system('echo "'+list+'" >> savepole.txt')
def xysave(y,x):
	xy="["+str(y)+", "+str(x)+"],"
	cd='cd /home/dmodv/git_project/testing/ && '
	os.system(cd+"touch savexy.txt")
	os.system('echo "'+xy+'" >> savexy.txt')
def saveall(pole,y,x):
	rasb(pole)
	xysave(y,x)
	
for p in range(1):
	for i in range(3):
		for j in range(3):
			board[i][j]=2
			saveall(board,i,j)


