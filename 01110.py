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

[
    [1,1,1,1],
    [1,1,1,1],
    [0,0,0,0],
    [0,0,0,0],
    [1,1,1,1],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]


f = np.array([1, 0, 1, 0, 1, 0, 1, 0])

model = keras.Sequential()
model.add(Dense(units=1, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

history = model.fit(c, f, epochs=500, verbose=0)