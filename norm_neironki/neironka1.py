"""""
#Задача: Нейросеть решает насущную для меня делему, покупать квас или нет.
# 
#  
# Критерии(input):
# 1. Наличие денег
# 2. Как близко магазин К/Б, т.к. там самый вкусный по моему мнению квас.
# 3. Есть ли он там сейчас в наличии.
# 4. Хочу ли я пить.


# Вывод(output):
1. нет денег бан
2. далеко бан
3. нет в наличии БАААН
4. я всегда хочу пить
"""
#Итак пошёл код, для начало сделаем кейс на котором будет трениться моя нейронка


import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import Sequential
from keras.layers import Dense
from tensorflow import keras

c=np.array([[1,1,1,1],
   [1,1,1,0],
   [1,1,0,1],
   [1,0,1,0],
   [1,0,1,1],
   [0,1,1,1],
   [0,0,0,0],
   [0,0,0,1],
   [1,0,1,0],
   [1,0,0,0]])
f=np.array([1,1,0,0,1,0,0,0,0,0])
#c = np.array([-40,-10,0,8,15,22,38])
#f = np.array([-40,14,32,46,59,72,100])
model = keras.Sequential()
model.add(Dense(units=1, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

history = model.fit(c, f, epochs=600, verbose=0)

plt.plot(history.history["loss"])
plt.grid(True)
plt.show()


""""Далее мы запросим данные и сделаем на их основе предсказание"""

def inputData():
  print("Ввод 1 или 0 !!!")
  a=int(input("Есть деньги?  "))
  b=int(input("Ты сейчас находишся близко к магазину?  "))
  c=int(input("А в магазине есть квас?!  "))
  d=int(input("Ты действительно хочешь пить o_.  ?  "))
  array=[a,b,c,d]
  return array

def otv(array):
  ii=array[0][0]
  if ii>0.5:
    return "\n\nРаз так, то конечно покупай)"
  elif ii<0.5:
    return "\n\nТы попьёшь кваса, но не в этот раз("
  else:
    return "\n\nТы чё тут ввёл, оно не работает О_О"

    
reshenie=model.predict([inputData()])
print(otv(reshenie))