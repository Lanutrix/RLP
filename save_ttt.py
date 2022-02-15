# from os import system as sys
from subprocess import check_output as sys
import re
def save(pole, x, y):
    
    try:
        file=open("statos.txt", "r")
        print(2)
    except:
        file=open("statos.txt", "w+")
        print(0)
save(1,1,1)
i = sys('pwd', universal_newlines=True)
print(i,type(i))